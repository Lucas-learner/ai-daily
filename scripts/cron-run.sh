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

# 防止 cron 任务重叠执行（如果前一天任务未结束，跳过当天）
if [ -e "$LOCK_FILE" ]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: 检测到锁文件 $LOCK_FILE，跳过本次执行" >> "$LOG_FILE"
  exit 0
fi
trap 'rm -f "$LOCK_FILE"' EXIT
touch "$LOCK_FILE"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 系统 cron 触发 AI 日报任务"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 工作目录: $PROJECT_DIR"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] kimi: $KIMI_BIN"

  # -p: 非交互式单条 prompt，cron 环境下可直接执行
  "$KIMI_BIN" -p "执行ai日报任务" 2>&1 || {
    rc=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: kimi 日报任务退出码 $rc"
    exit $rc
  }

  # 同步到 GitHub Pages（与 iCloud 解耦，避免 iCloud 阻塞影响网页发布）
  "$PROJECT_DIR/scripts/sync-to-github.sh" "$YEAR_MONTH" 2>&1 || {
    rc=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: GitHub Pages 同步退出码 $rc"
  }

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 系统 cron AI 日报任务完成"
} >> "$LOG_FILE" 2>&1
