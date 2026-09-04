#!/bin/bash
set -euo pipefail

# AI日报系统级 cron 入口
# 用法：由 crontab 每天调用一次

PROJECT_DIR="/Users/macmini/projects/skills/ai-daily"
KIMI_BIN="/Users/macmini/.kimi-code/bin/kimi"
LOG_DIR="$PROJECT_DIR/logs"
DATE="$(date +%Y-%m-%d)"
YEAR_MONTH="$(date +%Y-%m)"
LOG_FILE="$LOG_DIR/ai-daily-$(date +%Y%m%d).log"
LOCK_FILE="$PROJECT_DIR/.ai-daily-cron.lock"

mkdir -p "$LOG_DIR"
cd "$PROJECT_DIR"

# 加载本地配置（NOTIFY_TO / NOTIFY_ON_SUCCESS），不存在则静默跳过通知
if [ -f "$PROJECT_DIR/scripts/config.sh" ]; then
  # shellcheck source=/dev/null
  . "$PROJECT_DIR/scripts/config.sh"
fi
NOTIFY_TO="${NOTIFY_TO:-}"
NOTIFY_ON_SUCCESS="${NOTIFY_ON_SUCCESS:-0}"

# 通知：始终写日志；配置了 NOTIFY_TO 时同时发 iMessage
notify() {
  local msg="$1"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] NOTIFY: $msg" >> "$LOG_FILE"
  if [ -n "$NOTIFY_TO" ]; then
    "$PROJECT_DIR/scripts/send-imessage.sh" "$NOTIFY_TO" "$msg" >> "$LOG_FILE" 2>&1 || true
  fi
}

# 防止 cron 任务重叠执行（如果前一天任务未结束，跳过当天）
if [ -e "$LOCK_FILE" ]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: 检测到锁文件 $LOCK_FILE，跳过本次执行" >> "$LOG_FILE"
  notify "⚠️ AI日报 $DATE 跳过：检测到残留锁文件（可能昨日任务未正常结束）"
  exit 0
fi
trap 'rm -f "$LOCK_FILE"' EXIT
touch "$LOCK_FILE"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 系统 cron 触发 AI 日报任务"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 工作目录: $PROJECT_DIR"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] kimi: $KIMI_BIN"

  # 昨日缺席检测：昨天没有日志说明昨天没跑（机器休眠/关机等），通知但不阻塞今日任务
  YESTERDAY="$(date -v-1d +%Y-%m-%d)"
  if [ ! -f "$LOG_DIR/ai-daily-$(date -v-1d +%Y%m%d).log" ]; then
    notify "⚠️ AI日报：昨日（${YESTERDAY}）未执行任务（无日志，可能机器休眠）。今日任务继续。"
  fi

  # -p: 非交互式单条 prompt，cron 环境下可直接执行
  "$KIMI_BIN" -p "执行ai日报任务" 2>&1 || {
    rc=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: kimi 日报任务退出码 $rc"
    notify "❌ AI日报 ${DATE} 失败：kimi 退出码 ${rc}。最后日志：$(tail -n 3 "$LOG_FILE" | tr '\n' ' ' | cut -c1-200)"
    exit $rc
  }

  # 同步到 GitHub Pages（与 iCloud 解耦，避免 iCloud 阻塞影响网页发布）
  "$PROJECT_DIR/scripts/sync-to-github.sh" "$YEAR_MONTH" 2>&1 || {
    rc=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: GitHub Pages 同步退出码 $rc"
    notify "⚠️ AI日报 ${DATE}：日报已生成，但 GitHub Pages 同步失败（退出码 ${rc}）"
  }

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 系统 cron AI 日报任务完成"

  # 成功简报（默认关闭，config.sh 中 NOTIFY_ON_SUCCESS=1 开启）
  if [ "$NOTIFY_ON_SUCCESS" = "1" ]; then
    COUNT=$(awk -v d="$DATE" '
      $0 ~ ("^## 【" d "】") { f=1; next }
      f && /^## 【/ { exit }
      f && /- \*\*来源\*\*/ { n++ }
      END { print n+0 }
    ' "$PROJECT_DIR/reports/$YEAR_MONTH.md" 2>/dev/null || echo "?")
    notify "✅ AI日报 $DATE 完成，精选 ${COUNT} 条，已同步。"
  fi
} >> "$LOG_FILE" 2>&1
