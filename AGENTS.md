# AI日报项目 Agent 指令

## 项目目标

通过 `cron + kimi-code` 定时生成 AI 行业日报，并自动归档、去重与同步。

## 关键路径

1. **工作目录**：`/Users/macmini/projects/skills/ai-daily`
2. **去重追踪器**：`memory/ai-news-tracker.md`
3. **日报存储**：`reports/YYYY-MM.md`（每月一个文件，日期区块逆序）
4. **日志**：`logs/ai-daily-YYYYMMDD.log`
5. **iCloud 可视化同步**：`~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/`
6. **GitHub Pages 公开站点**：`https://lucas-learner.github.io/ai-daily/`
7. **GitHub 同步兜底脚本**：`scripts/github-api-push.py`（当 `git push` 因网络/SSL 失败时，通过 GitHub Contents API 直接更新 `docs/` 文件）

## 执行原则

- 所有文件操作优先使用项目内的 helper 脚本，减少直接 Edit/Write 的出错概率。
- 日报生成后必须更新 `memory/ai-news-tracker.md`，只保留最近 30 天主题。
- 每月 1 日先执行上个月归档（生成月度总结 + HTML），再开始当月日报。
- 自动化过程中遇到外部服务阻塞（如 iCloud 访问失败、GitHub push 超时、网络异常），应主动尝试多种方法解决，而不是直接跳过或放弃。常见手段包括：重试、使用备用同步路径、改用 API 直接更新、记录错误并继续后续步骤等。

## 触发词

当用户或 cron 提示中出现以下表达时，执行日报任务：

- "执行ai日报任务"
- "生成AI日报"
- "跑一下日报"
- "今天AI新闻"
- "ai daily"

## 定时任务维护

项目同时使用两层定时触发：

1. **kimi-code 内置 CronCreate**（session 级，便于测试）
   - 仅对当前 session 生效，`kimi resume` 可恢复，新 session 不继承。
   - 循环任务 7 天后自动过期，需定期重新创建。
2. **系统级 crontab**（生产兜底）
   - 入口脚本：`scripts/cron-run.sh`
   - 执行命令：`/Users/macmini/.kimi-code/bin/kimi -p "执行ai日报任务"`
   - 注意：cron 环境请使用 `-p` 单条 prompt 模式；`-y`/`--yolo` 与 `-p`/`--prompt` 在 CLI 中不可同时使用
   - 默认时间：`7 8 * * *`（每天 08:07，Asia/Shanghai）
   - 日志：`logs/ai-daily-YYYYMMDD.log`

新增或迁移机器后，优先确保系统 crontab 存在；kimi-code 内置 cron 仅用于临时调试。

## 输出要求

- 每月日报文件使用二级日期标题 `## 【YYYY-MM-DD】`
- 分类使用三级标题：`### 🔥 Breaking`、`### 📌 核心动态`、`### 📎 其他要闻`、`### 💡 今日洞察`
- 新闻标题加粗 `**标题**`
- **每条新闻必须附带可点击的来源链接**：`- **来源**：[来源名](URL) | **时间**：X月X日`；多个来源时用 `/` 分隔多个链接
- 新日期追加到当月文件最顶部（逆序）
