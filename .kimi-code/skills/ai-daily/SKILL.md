# AI Daily Report - AI行业日报生成（cron + kimi-code 版）

自动生成AI行业日报，采集多源信息，智能去重，输出精选内容，并按月汇总存储。

## 触发命令

用户说以下任意一种表达时，执行此任务：
- "执行ai日报任务"
- "生成AI日报"
- "跑一下日报"
- "今天AI新闻"
- "ai daily"

## 前置检查

1. **工作目录**：`/Users/macmini/projects/skills/ai-daily`
2. **检查日期**：若今天是当月 1 日，先执行**月度归档流程**（见下方），再生成当日日报。
3. **读取去重追踪器**：`memory/ai-news-tracker.md`，获取最近 30 天已报道主题。

## 月度归档流程（仅每月 1 日执行）

1. 确定上个月：`YYYY-MM-prev`（例如今天是 2026-07-01，则处理 2026-06）。
2. 读取 `reports/YYYY-MM-prev.md`。
3. 基于整月内容，生成月度总结，需包含：
   - 本月 Top 5-8 重大事件
   - 3 条关键趋势
   - 高频公司/技术标签：**先跑统计脚本拿确定性计数，LLM 只做解读不做计数**：
     ```bash
     bash /Users/macmini/projects/skills/ai-daily/scripts/query-items.sh --month YYYY-MM-prev --stats
     ```
     （统计该月 `data/items/*.jsonl` 的分类分布、来源分布与条目总量；公司/技术标签的归纳在此数据之上进行）
   - 与上月的延续或变化
4. 将总结写入临时文件 `/tmp/ai-daily-summary-YYYY-MM-prev.md`。
5. 调用脚本归档：
   ```bash
   bash /Users/macmini/projects/skills/ai-daily/scripts/archive-month.sh YYYY-MM-prev /tmp/ai-daily-summary-YYYY-MM-prev.md
   ```
6. 脚本会自动：
   - 将总结插入到 `reports/YYYY-MM-prev.md` 最顶部
   - 生成 `reports/YYYY-MM-prev.html`
   - 同步 `.md` 和 `.html` 到 iCloud `数据同步/ai daily/`

## 每日日报流程

### 第一步：读取已报道主题

读取 `/Users/macmini/projects/skills/ai-daily/memory/ai-news-tracker.md`，获取最近 30 天已报道的主题列表。

### 第二步：数据采集

**时间窗定义（先明确，再采集）**：日报的"今日"= **前一日 08:00 至当日 08:00（北京时间）**，与 08:00 的系统 cron 触发时间对齐。采集、筛选、写入都以此窗口为准；窗口外但重要的内容归入最近一期日报，不跨期重复。

**混合采集模式（固定源为主，搜索为辅）：**

1. **先跑 RSS 固定源采集脚本**，产出时间窗内候选池：
   ```bash
   python3 /Users/macmini/projects/skills/ai-daily/scripts/fetch-rss.py --hours 25 > /tmp/ai-daily-rss-$(date +%Y%m%d).jsonl
   ```
   源清单在 `scripts/rss-feeds.txt`（国内：雷峰网/InfoQ中文/36氪/量子位/IT之家；海外：TechCrunch/The Verge/Ars Technica/OpenAI Blog/MIT Technology Review/Hugging Face Blog）。增删来源只改该文件，无需改代码。单源失败脚本只告警（stderr）不中断，属正常现象；候选为 0 或明显偏少时加大 WebSearch 比重。
2. **再按 AGENTS.md「配额控制」派 4 个子 agent**：优先从 RSS 候选池挑选本方向条目（Read/Grep 读 `/tmp/ai-daily-rss-*.jsonl`，不消耗搜索预算），WebSearch 用于补充 RSS 未覆盖的重大突发与一手报道（Reuters/Bloomberg/FT/The Information 等）。
3. **方向覆盖要求**：子 agent 1 须显式覆盖论文/研究类（`paper` 类长期缺失即视为采集遗漏）；子 agent 4 须覆盖中文垂直媒体（36氪/量子位/雷峰网/IT之家等）与国产芯片动态。

**来源可信度要求（硬性）：**
- 事实归属以官方公告为准（时间、金额、名称）；**性能/效果/规模类声明只有官方来源时，正文必须带"官方称/公司披露"字样**，"信号"行不得把未验证声明当作既定事实展开。
- **独立信源定义**：两个信源必须在编辑上独立于报道对象——官方公告 + 其转载/转述只算一个信源。
- **聚合站/内容农场禁止进入 jsonl 与日报正文**（写入时由 `add-daily-items.sh` 强制剔除）：`scripts/aggregator-blacklist.txt` 所列域名（killtheai、buildfastwithai、aiweekly、readaitime、aidapted、smzdm 等）。这类站点只能作为线索，必须回溯到原始来源链接。
- **语言-信源匹配**：中国相关事件可用中文垂直媒体作一手源（36氪/量子位/雷峰网首发的中国企业新闻）；海外事件必须链英文原始来源，中文翻译稿只能作佐证、不能作唯一信源。
- 重要新闻尽量提供两个独立信源（`/` 分隔多个链接）；无法验证真实性的，标记"据报道称"并降级为"其他要闻"。

### 第三步：去重筛选（关键）

**严格规则：**
- **URL 精确去重（脚本级，先做）**：采集后先把候选条目的 URL 与历史数据比对，命中即排除，不进入语义判断：
  ```bash
  # 候选 URL 列表逐条检查（命中任一来源即视为已报道）
  grep -RF --include='*.jsonl' -e "$URL" /Users/macmini/projects/skills/ai-daily/data/items/ \
    || grep -F "$URL" /Users/macmini/projects/skills/ai-daily/memory/ai-news-tracker.md
  ```
- 如果新闻主题与 `ai-news-tracker.md` 中记录的主题高度相似（同一公司 + 同一事件线），**直接跳过**（语义去重，LLM 判断）
- 除非是同一事件的**重大突破**（如昨天"拒绝"今天"被制裁"），可作为跟进简讯，但不占主条数
- 优先选择**全新公司/全新产品/全新技术**的报道

**主题相似性判断示例：**
| 已报主题 | 新内容 | 操作 |
|----------|--------|------|
| Anthropic拒绝五角大楼 | Anthropic与五角大楼冲突升级 | ❌ 跳过 |
| Perplexity Computer发布 | Perplexity Computer功能详解 | ❌ 跳过 |
| - | 全新公司/产品/技术 | ✅ 可报 |

### 第四步：动态质量判断

| 级别 | 标准 | 处理方式 |
|------|------|----------|
| S级 | 重大技术突破、重磅产品发布、头部公司战略调整，**且至少有一个编辑上独立的信源**（非官方、非官方稿转载） | 必报，放 Breaking |
| S级（仅官方口径） | 同上但无独立信源（如华为/智谱仅官方披露的重要发布） | 最高进核心动态，可置顶，正文标注"官方口径" |
| A级 | 重要论文、开源模型更新、基础设施变化 | 核心动态 |
| B级 | 行业分析、观点评论 | 仅保留视角独特的 |
| - | 公关软文、纯情绪输出、已报道主题的跟进 | ❌ 排除 |

### 第五步：生成日报内容

**格式规范（必须严格遵守）：**

| 元素 | 格式要求 | 示例 |
|------|----------|------|
| **日期标题** | 二级标题 `## 【日期】` | `## 【2026-06-23】` |
| **分类标题** | 三级标题 `###` | `### 🔥 Breaking` |
| **新闻标题** | 加粗 `**标题**` | `**OpenAI 发布 GPT-5.5**` |
| **正文** | 普通文本 + 列表项 | `- 支持文本、图像、视频` |
| **来源** | 每条注明来源，使用可点击链接 | `- **来源**：[TechCrunch](https://techcrunch.com/...) | **时间**：X月X日` |

**内容结构：**
```markdown
*本期覆盖 M月D日 08:00 至 M月D日 08:00（北京时间）。*

### 🔥 Breaking

**🌍 新闻标题（独立加粗行，带 Emoji 前缀）**

- **来源**：[来源名](https://example.com/article) | **时间**：X月X日
- 详情段落：补充数字、背景、与往日报道的呼应
- 信号：……（一句话分析）

---

**🌍 另一条 Breaking**

- **来源**：……

### 📌 核心动态

（同 Breaking 条目格式，条目间用 `---` 分隔）

### 📎 其他要闻

- **[单行标题，内嵌来源链接](URL)**：一句点评。

### 💡 今日洞察

今日AI行业呈现X大趋势：
1. **趋势一**：详细阐述...
2. **趋势二**：详细阐述...
3. **趋势三**：详细阐述...
```

**格式要求：**
- 日期区块首行写时间窗说明：`*本期覆盖 M月D日 08:00 至 M月D日 08:00（北京时间）。*`（斜体）。
- Breaking/核心动态条目：标题为独立加粗行并带 Emoji 前缀，下接来源行、详情段落与"信号："分析行；**条目之间用 `---` 分隔**。
- 其他要闻为单行条目（标题内嵌来源链接 + 一句点评），条目间不加 `---`。禁止只写一句概述的简略风格。
- **来源链接**：每条新闻必须提供至少一个可点击的原始来源 URL，格式为 `[来源名](URL)`；若参考了多个来源，用 `/` 分隔多个链接（如 `[TechCrunch](URL1) / [The Verge](URL2)`）。
- 不要在条目中添加 `> 采集时间`、`> 信息来源`、`> 🔗 来源链接` 等元信息行。
- 每日精选 5-8 条，必须有 `### 💡 今日洞察` 段落。

**同时输出条目 JSONL（结构化数据层）：**

除日报正文外，把**完整采集池**（含未入选条目）写成 JSONL 临时文件 `/tmp/ai-daily-YYYY-MM-DD-items.jsonl`，每行一条：

```json
{"title":"中文标题","url":"https://原文链接","source":"来源名","publishedAt":"ISO 8601 或 null","category":"ai-models","grade":"S","selected":true}
```

字段约定：
- 必有：`title` / `url` / `source` / `selected`
- 可空：`publishedAt` / `category`（不确定时写 `null`）
- `category` 固定五类：`ai-models`（模型发布/更新）/ `ai-products`（产品发布/更新）/ `industry`（行业动态）/ `paper`（论文研究）/ `tip`（技巧与观点）
- `grade`：`S` / `A` / `B`（与第四步定级一致）
- `selected`：进入日报正文（精选 5-8 条）为 `true`，其余为 `false`——**落选条目也保留**，供本地检索与月度统计使用

### 第六步：写入月报文件

1. 将生成的日报内容（不含日期标题）写入临时文件，例如 `/tmp/ai-daily-YYYY-MM-DD-body.md`。
2. 调用脚本追加到月报顶部：
   ```bash
   bash /Users/macmini/projects/skills/ai-daily/scripts/add-daily-entry.sh YYYY-MM-DD /tmp/ai-daily-YYYY-MM-DD-body.md
   ```
3. 脚本会自动：
   - 若 `reports/YYYY-MM.md` 不存在则创建
   - 在文件顶部插入 `## 【YYYY-MM-DD】` 和内容
   - 保持整月文件逆序
4. 写入结构化条目（JSONL 数据层）：
   ```bash
   bash /Users/macmini/projects/skills/ai-daily/scripts/add-daily-items.sh YYYY-MM-DD /tmp/ai-daily-YYYY-MM-DD-items.jsonl
   ```
   脚本会校验每行 JSON 的必填字段，并剔除聚合站黑名单来源与历史重复 URL（剔除只告警不阻塞，字段格式错误则整批拒绝），再追加到 `data/items/YYYY-MM-DD.jsonl`。

### 第七步：同步到 iCloud

调用脚本：
```bash
bash /Users/macmini/projects/skills/ai-daily/scripts/sync-to-icloud.sh YYYY-MM
```

脚本会：
1. 复制 `reports/YYYY-MM.md` 和 `reports/YYYY-MM.html` 到：
   ```
   ~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/reports/
   ```
2. 生成当日「今日洞察」摘要到临时目录（`daily-summary.md/html` 只是中间产物，内嵌后即弃，不留存）。
3. 更新根目录的 `index.html` 索引页，并在顶部直接内嵌展示今日摘要内容。

### 第八步：更新追踪器

报道完成后，**必须**更新 `memory/ai-news-tracker.md`：

1. 添加今日日期和已报道主题（简洁格式）
2. 删除超过 30 天的旧记录
3. 主题格式：`公司-关键词-核心事实`（每行不超过 50 字符）
4. 每条必须带「来源 URL」列（取该主题最有代表性的一个原始链接），供 URL 级精确去重使用

示例：
```markdown
## 2026-06-23

| 话题关键词 | 首次报道日期 | 来源 URL | 简要描述 |
|-----------|-------------|---------|---------|
| OpenAI-GPT5.5-发布 | 2026-06-23 | https://openai.com/news/xxx | OpenAI发布GPT-5.5多模态大模型 |
| Google-Gemini-降价 | 2026-06-23 | https://blog.google/xxx | Google将AI Plus降至$4.99 |
```

### 第九步：记录日志

写日志到 `logs/ai-daily-YYYYMMDD.log`：
```
[YYYY-MM-DD HH:MM:SS] 日报生成开始
[YYYY-MM-DD HH:MM:SS] 采集来源：...
[YYYY-MM-DD HH:MM:SS] 精选条数：X
[YYYY-MM-DD HH:MM:SS] 已更新 reports/YYYY-MM.md
[YYYY-MM-DD HH:MM:SS] 已同步 iCloud
[YYYY-MM-DD HH:MM:SS] 日报生成完成
```

### 第十步：返回给用户

只返回「今日洞察」部分作为摘要：
```
📅 AI日报洞察 | YYYY-MM-DD

今日AI行业呈现X大趋势：
1. **趋势一**：...
2. **趋势二**：...
3. **趋势三**：...

📊 今日精选 X 条 | 已保存至 reports/YYYY-MM.md 并同步 iCloud
```

## 约束

| 约束项 | 规则 |
|--------|------|
| 时间范围 | 只保留时间窗内（前一日 08:00 至当日 08:00，北京时间）内容 |
| 数量控制 | 每日 5-8 条精华 |
| 去重 | URL 精确去重（add-daily-items.sh 强制，含历史库与黑名单剔除）+ 语义去重（同公司同事件线跳过，LLM 判断） |
| 主题格式 | 公司-关键词-核心事实 |
| Token优化 | 跟踪文件只存主题不存详情 |

## 错误处理

若任何步骤失败：
1. **不要写入半成品文件**到 `reports/` 或 `memory/`。
2. 将错误信息写入 `logs/error-YYYYMMDD.log`：
   ```
   [YYYY-MM-DD HH:MM:SS] ERROR: 失败步骤描述
   [YYYY-MM-DD HH:MM:SS] 原因：...
   ```
3. 如脚本返回非零退出码，立即停止后续步骤。
4. 向用户返回简洁的失败说明，不要伪造日报内容。

## 文件位置

- 跟踪文件：`/Users/macmini/projects/skills/ai-daily/memory/ai-news-tracker.md`
- 结构化条目：`/Users/macmini/projects/skills/ai-daily/data/items/YYYY-MM-DD.jsonl`（完整采集池，含未入选条目）
- RSS 固定源采集：`scripts/fetch-rss.py`（源清单 `scripts/rss-feeds.txt`，增删来源改清单即可）
- 来源黑名单：`scripts/aggregator-blacklist.txt`（聚合站域名，写入 jsonl 时被剔除）
- 本地检索：`scripts/query-items.sh --q 关键词 [--days N | --month YYYY-MM] [--category 五类之一] [--all] [--stats]`
- 月报文件：`/Users/macmini/projects/skills/ai-daily/reports/YYYY-MM.md`
- 可视化文件：`/Users/macmini/projects/skills/ai-daily/reports/YYYY-MM.html`
- iCloud 同步：`~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/`
- 执行日志：`/Users/macmini/projects/skills/ai-daily/logs/ai-daily-YYYYMMDD.log`
