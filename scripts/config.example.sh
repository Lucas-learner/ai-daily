#!/bin/bash
# AI日报共享配置模板。
# 使用方法：cp scripts/config.example.sh scripts/config.sh，然后填入真实值。
# scripts/config.sh 已被 .gitignore 忽略，不会进入 git（避免手机号等隐私泄漏到公开仓库）。

# iMessage 通知接收人（手机号或邮箱）。留空则不发送任何通知。
# 失败时始终通知（若已配置）；用于 cron-run.sh 的失败告警与昨日缺席检测。
NOTIFY_TO=""

# 成功时是否也发送一行简报：1 发送 / 0 不发送
NOTIFY_ON_SUCCESS=0

# 备用 CLI agent。默认使用 OpenCode + DeepSeek Flash。
# 可替换为其他支持非交互执行、并接受末尾 prompt 参数的 CLI；参数用空格分隔。
# 示例：FALLBACK_AGENT_BIN="/usr/local/bin/claude"，FALLBACK_AGENT_ARGS="-p"
FALLBACK_AGENT_BIN="/Users/macmini/.opencode/bin/opencode"
FALLBACK_AGENT_ARGS="run --standalone --auto --model deepseek/deepseek-flash"
