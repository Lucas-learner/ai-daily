# AI日报项目 Agent 指令

## 项目目标

通过 `cron + kimi-code` 定时生成 AI 行业日报，并自动归档、去重与同步。

## 关键路径

1. **工作目录**：`/Users/macmini/projects/skills/ai-daily`
2. **去重追踪器**：`memory/ai-news-tracker.md`（含「来源 URL」列，供 URL 级精确去重）
3. **日报存储**：`reports/YYYY-MM.md`（每月一个文件，日期区块逆序）
4. **结构化条目层**：`data/items/YYYY-MM-DD.jsonl`（完整采集池，含未入选条目；`selected` 字段区分精选/全部）
5. **日志**：`logs/ai-daily-YYYYMMDD.log`
6. **iCloud 可视化同步**：`~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/`
7. **GitHub Pages 公开站点**：`https://lucas-learner.github.io/ai-daily/`
8. **GitHub 同步兜底脚本**：`scripts/github-api-push.py`（当 `git push` 因网络/SSL 失败时，通过 GitHub Contents API 直接更新 `docs/` 文件）
9. **docs/ 静态发布**：`scripts/update-github-pages.py` 会确保 `docs/.nojekyll` 存在，禁用 Jekyll，避免 `jekyll-github-metadata` 调用 GitHub API 时偶发 503 导致构建失败；同时调用 `scripts/build_daily_pages.py` 从 `data/items/*.jsonl` 生成 `docs/days/YYYY-MM-DD.html` 按日浏览页（分类筛选 + 精选/全部切换，data/items 为空时不生成、索引页也不显示入口）
10. **站点样式**：各页面共享 `scripts/page_style.py`（卡片式设计、暗色模式、月报日期 TOC/锚点）；改样式只改这个文件，不要手改 docs/ 下的生成产物
10. **通知配置**：`scripts/config.sh`（已 gitignore，含 iMessage 接收人 `NOTIFY_TO`；模板见 `scripts/config.example.sh`）
11. **本地检索**：`scripts/query-items.sh --q 关键词 [--days N | --month YYYY-MM] [--category 五类之一] [--all] [--stats]`

## 执行原则

- 所有文件操作优先使用项目内的 helper 脚本，减少直接 Edit/Write 的出错概率。
- 日报生成后必须同时更新两处：`memory/ai-news-tracker.md`（只保留最近 30 天主题）和 `data/items/YYYY-MM-DD.jsonl`（经 `scripts/add-daily-items.sh` 校验写入，含未入选条目）。
- 时间窗定义：日报的"今日"= 前一日 08:00 至当日 08:00（北京时间），与 08:07 cron 对齐；采集与筛选以此窗口为准。
- 去重分两层：先 URL 精确去重（脚本级 grep -F 比对 data/items/ 与 tracker），再 LLM 语义去重。
- 每月 1 日先执行上个月归档（生成月度总结 + HTML），再开始当月日报；月度统计（分类/来源分布）用 `query-items.sh --month YYYY-MM --stats` 出数，LLM 只做解读。
- 自动化过程中遇到外部服务阻塞（如 iCloud 访问失败、GitHub push 超时、网络异常），应主动尝试多种方法解决，而不是直接跳过或放弃。常见手段包括：重试、使用备用同步路径、改用 API 直接更新、记录错误并继续后续步骤等。
- 失败必通知：`cron-run.sh` 在 kimi 失败、GitHub 同步失败、昨日缺席、锁文件残留时会发 iMessage 告警（需配置 `scripts/config.sh` 的 `NOTIFY_TO`）；不要删除这些告警调用。

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
