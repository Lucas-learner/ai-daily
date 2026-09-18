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
9. **docs/ 静态发布**：`scripts/update-github-pages.py` 会确保 `docs/.nojekyll` 存在，禁用 Jekyll，避免 `jekyll-github-metadata` 调用 GitHub API 时偶发 503 导致构建失败
10. **月报 HTML 兜底**：`sync-to-icloud.sh` / `sync-to-github.sh` 在同步前会自动用 `md-to-html.py` 重新生成本月 `reports/YYYY-MM.html`，日报任务写稿后无需再手动执行 HTML 再生成；GitHub 推送自带重试 + API 兜底
11. **站点样式**：各页面共享 `scripts/page_style.py`（卡片式设计、暗色模式、月报日期 TOC/锚点）；改样式只改这个文件，不要手改 docs/ 下的生成产物
12. **通知配置**：`scripts/config.sh`（已 gitignore，含 iMessage 接收人 `NOTIFY_TO`；模板见 `scripts/config.example.sh`）
13. **本地检索**：`scripts/query-items.sh --q 关键词 [--days N | --month YYYY-MM] [--category 五类之一] [--all] [--stats]`
14. **RSS 固定源采集**：`scripts/fetch-rss.py`（源清单 `scripts/rss-feeds.txt`，增删来源只改清单；聚合站黑名单 `scripts/aggregator-blacklist.txt`）

## 执行原则

- 所有文件操作优先使用项目内的 helper 脚本，减少直接 Edit/Write 的出错概率。
- 日报生成后必须同时更新两处：`memory/ai-news-tracker.md`（只保留最近 30 天主题）和 `data/items/YYYY-MM-DD.jsonl`（经 `scripts/add-daily-items.sh` 校验写入，含未入选条目）。
- 时间窗定义：日报的"今日"= 前一日 08:00 至当日 08:00（北京时间），与 08:00 cron 对齐；采集与筛选以此窗口为准。
- 去重分两层：URL 精确去重由 `add-daily-items.sh` 写入时强制执行（比对 `data/items/` 全量历史，命中即剔除；同时剔除聚合站黑名单来源），采集阶段仍可先用 `grep -F` 粗查 `data/items/` 与 tracker 避免无效写作；再 LLM 语义去重（同公司同事件线跳过）。
- 每月 1 日先执行上个月归档（生成月度总结 + HTML），再开始当月日报；月度统计（分类/来源分布）用 `query-items.sh --month YYYY-MM --stats` 出数，LLM 只做解读。
- 自动化过程中遇到外部服务阻塞（如 iCloud 访问失败、GitHub push 超时、网络异常），应主动尝试多种方法解决，而不是直接跳过或放弃。常见手段包括：重试、使用备用同步路径、改用 API 直接更新、记录错误并继续后续步骤等。
- 本机 shell 与系统代理（Clash 127.0.0.1:7897）上游可能失效，表现为所有 HTTPS 走代理报 `SSL_ERROR_SYSCALL` 但 `--noproxy '*'` 直连畅通。sync-to-github.sh 已内置「先绕代理直连、再走默认代理」的降级；手动排查网络时先用 `curl --noproxy '*' -I https://github.com` 判断是代理问题还是 GitHub 本身不可达。
- 失败必通知：`cron-run.sh` 在 kimi 失败、GitHub 同步失败、昨日缺席、锁文件残留时会发 iMessage 告警（需配置 `scripts/config.sh` 的 `NOTIFY_TO`）；不要删除这些告警调用。

## 配额控制（199 套餐）

订阅额度有限（单次任务实测曾吃掉 5h 窗口的 40%），采集与写作必须按以下约束执行，目标单次任务 ≤ 20% 窗口配额：

- **混合采集（先 RSS 后搜索）**：主 agent 先跑 `python3 scripts/fetch-rss.py --hours 25 > /tmp/ai-daily-rss-$(date +%Y%m%d).jsonl` 生成固定源候选池（源清单 `scripts/rss-feeds.txt`），再派子 agent；子 agent 优先用 Read/Grep 从候选池挑选本方向条目（不耗搜索预算），搜索仅补充候选池未覆盖的重大突发与一手报道。
- **子 agent 固定 4 个**，用 AgentSwarm 一次并行发出，不再按 7 个方向拆分：
  1. 【前沿模型与产品·机器人科研】OpenAI / Anthropic / Google / Meta / xAI 等的模型发布、产品、API/价格、故障争议 + 人形机器人、自动驾驶、AI for Science。**须显式覆盖论文/研究类候选（paper）**，长期缺 paper 类即视为采集遗漏。
  2. 【产业商业·国际】融资、IPO、并购、财报、估值、重磅合作、高管变动 + 日韩欧中东（Mistral、软银、ASML、HUMAIN、G42 等）动态。
  3. 【芯片与算力】NVIDIA / AMD / Intel / 台积电 / 存储 / 数据中心 / 电力与网络设备。
  4. 【政策监管·中国AI】各国 AI 立法、监管、重大诉讼、安全事件 + 中国大模型/国产芯片/国内资本动态。**须覆盖中文垂直媒体**（36氪/量子位/雷峰网/IT之家等）。
- **来源硬规则**：聚合站/内容农场（`scripts/aggregator-blacklist.txt`：killtheai、buildfastwithai、aiweekly、readaitime、aidapted、smzdm 等）只能作线索，其 URL 禁止进入候选与 jsonl，必须回溯原始来源链接；写入时脚本会强制剔除。
- **每个子 agent 的搜索预算**：最多 6 次搜索，最多抓取 3 个网页全文，其余条目依据搜索摘要判断；产出 5–8 条候选即可收口，宁缺毋滥。
- **主 agent 写稿**：候选汇总后初稿一次成型，脚本写入/校验失败时针对修复，不做全量复读式自查；总校验轮数 ≤ 1。
- 抓取网页优先用 FetchURL 的正文提取结果，避免 Bash curl 拉取原始 HTML。

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
   - 执行命令：`/Users/macmini/.kimi-code/bin/kimi -p "执行ai日报任务" -m "kimi-code/kimi-for-coding"`（`-m` 固定本任务用 kimi-for-coding，不随全局 default_model 变动；实际由 cron-run.sh 以 `KIMI_MODEL_THINKING_EFFORT=low` 环境变量强制低思考强度，仅作用于本任务进程）
   - 注意：cron 环境请使用 `-p` 单条 prompt 模式；`-y`/`--yolo` 与 `-p`/`--prompt` 在 CLI 中不可同时使用
   - 默认时间：`0 8 * * *`（每天 08:00，Asia/Shanghai）
   - 日志：`logs/ai-daily-YYYYMMDD.log`

新增或迁移机器后，优先确保系统 crontab 存在；kimi-code 内置 cron 仅用于临时调试。

## 输出要求

- 每月日报文件使用二级日期标题 `## 【YYYY-MM-DD】`
- 分类使用三级标题：`### 🔥 Breaking`、`### 📌 核心动态`、`### 📎 其他要闻`、`### 💡 今日洞察`
- 新闻标题加粗 `**标题**`
- **每条新闻必须附带可点击的来源链接**：`- **来源**：[来源名](URL) | **时间**：X月X日`；多个来源时用 `/` 分隔多个链接
- **条目格式（Breaking/核心动态）**：标题为独立加粗行并带 Emoji 前缀，下接来源行、详情段落（补充数字/背景/与往日报道的呼应）与"信号："分析行，条目间用 `---` 分隔；其他要闻为单行条目（标题内嵌来源链接+一句点评）。禁止只写一句概述的简略风格
- 日期区块首行注明覆盖窗口：`*本期覆盖 M月D日 08:00 至 M月D日 08:00（北京时间）。*`
- 新日期追加到当月文件最顶部（逆序）
