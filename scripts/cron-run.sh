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
# 发送走本机共享通道 macos-notify（~/projects/tools/macos-notify/send-imessage.sh）
NOTIFY_SCRIPT="$HOME/projects/tools/macos-notify/send-imessage.sh"
notify() {
  local msg="$1"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] NOTIFY: $msg" >> "$LOG_FILE"
  if [ -n "$NOTIFY_TO" ]; then
    "$NOTIFY_SCRIPT" "$NOTIFY_TO" "$msg" >> "$LOG_FILE" 2>&1 || true
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

  # 过期文件清理：tmp/ 日报草稿保留 30 天，运行日志保留 60 天
  find "$PROJECT_DIR/tmp" -type f -mtime +30 -delete 2>/dev/null || true
  find "$LOG_DIR" -name "ai-daily-*.log" -mtime +60 -delete 2>/dev/null || true

  # 上月归档兜底：上月报告存在但缺月度总结时，要求 kimi 先补归档再写今日日报
  # （防止每月 1 日任务失败导致归档长期缺失，如 2026-07 拖到 9 月才手动补）
  LAST_MONTH="$(date -v-1m +%Y-%m)"
  PROMPT="执行ai日报任务"
  if [ -f "$PROJECT_DIR/reports/$LAST_MONTH.md" ] && ! grep -q "# ${LAST_MONTH} 月度总结" "$PROJECT_DIR/reports/$LAST_MONTH.md"; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 检测到上月（$LAST_MONTH）未归档，将在 prompt 中要求先补归档"
    PROMPT="执行ai日报任务。注意：检测到上月（${LAST_MONTH}）尚未归档（reports/${LAST_MONTH}.md 缺少月度总结）。请先按 AGENTS.md 流程补做上月归档（用 scripts/query-items.sh --month ${LAST_MONTH} --stats 出数撰写月度总结，再用 scripts/archive-month.sh ${LAST_MONTH} 归档），然后再生成今日日报。"
  fi

  # -p: 非交互式单条 prompt，cron 环境下可直接执行
  # -m: 本任务固定使用 kimi-for-coding，与全局 default_model 解耦
  # KIMI_MODEL_THINKING_EFFORT=low: 仅本进程强制低思考强度（省配额），不影响全局配置
  # 失败重试：网络/OAuth 瞬时故障常见（2026-08 曾因此连挂 14 天），最多 3 次、间隔 20 分钟；
  # 配额耗尽（usage limit）重试无意义，直接判失败
  RC=0
  for ATTEMPT in 1 2 3; do
    KIMI_MODEL_THINKING_EFFORT=low "$KIMI_BIN" -p "$PROMPT" -m "kimi-code/kimi-for-coding" 2>&1 && RC=0 || RC=$?
    if [ "$RC" -eq 0 ]; then
      break
    fi
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: kimi 日报任务第 ${ATTEMPT}/3 次执行失败，退出码 $RC"
    if tail -n 20 "$LOG_FILE" | grep -qi "usage limit"; then
      echo "[$(date '+%Y-%m-%d %H:%M:%S')] 检测到配额耗尽（usage limit），重试无意义，直接判失败"
      break
    fi
    if [ "$ATTEMPT" -lt 3 ]; then
      echo "[$(date '+%Y-%m-%d %H:%M:%S')] 20 分钟后重试（第 $((ATTEMPT+1))/3 次）..."
      sleep 1200
    fi
  done
  if [ "$RC" -ne 0 ]; then
    notify "❌ AI日报 ${DATE} 失败：kimi 退出码 ${RC}（已重试 ${ATTEMPT} 次）。最后日志：$(tail -n 3 "$LOG_FILE" | tr '\n' ' ' | cut -c1-200)"
    exit "$RC"
  fi

  # 同步到 GitHub Pages（与 iCloud 解耦，避免 iCloud 阻塞影响网页发布）
  "$PROJECT_DIR/scripts/sync-to-github.sh" "$YEAR_MONTH" 2>&1 || {
    rc=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: GitHub Pages 同步退出码 $rc"
    notify "⚠️ AI日报 ${DATE}：日报已生成，但 GitHub Pages 同步失败（退出码 ${rc}）"
  }

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 系统 cron AI 日报任务完成"

  # 成功简报（默认关闭，config.sh 中 NOTIFY_ON_SUCCESS=1 开启）
  # 统计当月文件最新有效日期区块（第一个含头条小节的区块）的条目数，空区块自动跳过
  if [ "$NOTIFY_ON_SUCCESS" = "1" ]; then
    COUNT=$(awk '
      /^## 【/ { if (in_target) exit; in_target=0 }
      /### 🔥 (Breaking|头条)/ { in_target=1 }
      in_target && /- \*\*来源\*\*/ { n++ }
      END { print n+0 }
    ' "$PROJECT_DIR/reports/$YEAR_MONTH.md" 2>/dev/null || echo "?")
    # 提取最新有效日期区块（跳过空区块）头条小节的前 2 条标题（兼容两种格式：独立标题行 / "- **标题**" 列表行；小节标题兼容旧 Breaking 与新 头条）
    BREAKING=$(REPORT="$PROJECT_DIR/reports/$YEAR_MONTH.md" python3 - <<'PYEOF'
import os, re
try:
    text = open(os.environ["REPORT"], encoding="utf-8").read()
    blocks = re.split(r'^## 【', text, flags=re.M)[1:]
    pat = re.compile(r'### 🔥 (?:Breaking|头条)')
    sec = next(pat.split(b)[1].split('### ')[0]
               for b in blocks if pat.search(b))
    titles = []
    for line in sec.splitlines():
        m = re.match(r'^[-•]\s*\*\*(.+?)\*\*', line) or re.match(r'^\*\*(.+?)\*\*\s*$', line.strip())
        if m and not m.group(1).startswith(('来源', '时间')):
            titles.append(m.group(1))
    print('\n'.join(f"{i}. {t}" for i, t in enumerate(titles[:2], 1)))
except Exception:
    pass
PYEOF
)
    if [ -n "$BREAKING" ]; then
      notify "✅ AI日报 ${DATE} 完成，最新一期精选 ${COUNT} 条，已同步。

今日头条：
${BREAKING}"
    else
      notify "✅ AI日报 ${DATE} 完成，最新一期精选 ${COUNT} 条，已同步。"
    fi
  fi
} >> "$LOG_FILE" 2>&1
