# AI日报项目 Agent 指令

## 项目目标

将原本由 OpenClaw 执行的 AI 行业日报任务，迁移到 `cron + kimi-code` 定时激发。

## 关键路径

1. **工作目录**：`/Users/macmini/projects/cron/ai-daily`
2. **去重追踪器**：`memory/ai-news-tracker.md`
3. **日报存储**：`reports/YYYY-MM.md`（每月一个文件，日期区块逆序）
4. **日志**：`logs/ai-daily-YYYYMMDD.log`
5. **iCloud 可视化同步**：`~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/`

## 执行原则

- 所有文件操作优先使用项目内的 helper 脚本，减少直接 Edit/Write 的出错概率。
- 日报生成后必须更新 `memory/ai-news-tracker.md`，只保留最近 30 天主题。
- 每月 1 日先执行上个月归档（生成月度总结 + HTML），再开始当月日报。
- OpenClaw 原始文件只读引用，不删除、不修改。

## 触发词

当用户或 cron 提示中出现以下表达时，执行日报任务：

- "执行ai日报任务"
- "生成AI日报"
- "跑一下日报"
- "今天AI新闻"
- "ai daily"

## 输出要求

- 每月日报文件使用二级日期标题 `## 【YYYY-MM-DD】`
- 分类使用三级标题：`### 🔥 Breaking`、`### 📌 核心动态`、`### 📎 其他要闻`、`### 💡 今日洞察`
- 新闻标题加粗 `**标题**`
- 新日期追加到当月文件最顶部（逆序）
