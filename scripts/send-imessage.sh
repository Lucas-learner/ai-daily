#!/bin/bash
set -euo pipefail

# 通过 macOS Messages 应用发送 iMessage
# 用法：send-imessage.sh "接收方手机号或邮箱" "要发送的消息"
# 示例：send-imessage.sh "+86 138 0000 0000" "📅 AI日报 | 2026-06-23"
# 示例：send-imessage.sh "your@icloud.com" "今日洞察摘要..."

RECIPIENT="${1:-}"
MESSAGE="${2:-}"

if [ -z "$RECIPIENT" ] || [ -z "$MESSAGE" ]; then
  echo "Usage: $0 <recipient_phone_or_email> <message>" >&2
  echo "Example: $0 \"+86 138 0000 0000\" \"hello world\"" >&2
  exit 1
fi

# 对 AppleScript 字符串进行转义：双引号 -> \"，反斜杠 -> \\
ESCAPED_MESSAGE=$(printf '%s' "$MESSAGE" | sed 's/\\/\\\\/g; s/"/\\"/g')
ESCAPED_RECIPIENT=$(printf '%s' "$RECIPIENT" | sed 's/\\/\\\\/g; s/"/\\"/g')

send_message() {
    local mode="$1"  # "background" 或 "foreground"
    if [ "$mode" = "foreground" ]; then
        # 前台激活并发送：当后台方式失败时使用，强制建立 iMessage 连接
        osascript <<EOF
tell application "Messages"
    activate
    delay 3
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "${ESCAPED_RECIPIENT}" of targetService
    send "${ESCAPED_MESSAGE}" to targetBuddy
end tell
EOF
    else
        # 后台方式：先尝试不抢夺焦点
        osascript <<EOF
tell application "Messages"
    if not running then
        launch
        delay 3
    end if
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "${ESCAPED_RECIPIENT}" of targetService
    send "${ESCAPED_MESSAGE}" to targetBuddy
end tell
EOF
    fi
}

# 尝试后台发送（不抢焦点）
if send_message "background"; then
    # osascript 成功执行不代表消息已送达，但先让其异步完成
    echo "iMessage send script executed (background mode)"
    exit 0
fi

# 后台失败则回退到前台激活方式
send_message "foreground"
