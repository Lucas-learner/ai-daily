#!/bin/bash
set -euo pipefail

# iMessage 发送稳定性测试脚本
# 用法：test-imessage.sh "接收方手机号或邮箱"
# 会连续发送 3 条测试消息，并报告耗时和结果

RECIPIENT="${1:-}"

if [ -z "$RECIPIENT" ]; then
  echo "Usage: $0 <recipient_phone_or_email>" >&2
  echo "Example: $0 \"+86 138 0000 0000\"" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SEND_SCRIPT="$SCRIPT_DIR/send-imessage.sh"

if [ ! -f "$SEND_SCRIPT" ]; then
  echo "Send script not found: $SEND_SCRIPT" >&2
  exit 1
fi

chmod +x "$SEND_SCRIPT"

echo "开始 iMessage 稳定性测试，接收方: $RECIPIENT"
echo "预计发送 3 条测试消息..."
echo ""

for i in 1 2 3; do
  MESSAGE="[AI日报测试 $i/3] 这是一条来自 ai-daily 项目的 iMessage 推送测试，发送时间：$(date '+%Y-%m-%d %H:%M:%S')。"
  echo "[$i/3] 发送中: $MESSAGE"
  START=$(date +%s)
  if "$SEND_SCRIPT" "$RECIPIENT" "$MESSAGE"; then
    END=$(date +%s)
    echo "[$i/3] ✅ 成功（耗时 $((END - START)) 秒）"
  else
    END=$(date +%s)
    echo "[$i/3] ❌ 失败（耗时 $((END - START)) 秒）" >&2
    exit 1
  fi
  echo ""
  [ "$i" -lt 3 ] && sleep 2
done

echo "全部测试完成。请检查接收方设备是否收到 3 条消息。"
