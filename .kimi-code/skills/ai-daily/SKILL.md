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

1. **工作目录**：`/Users/macmini/projects/cron/ai-daily`
2. **检查日期**：若今天是当月 1 日，先执行**月度归档流程**（见下方），再生成当日日报。
3. **读取去重追踪器**：`memory/ai-news-tracker.md`，获取最近 30 天已报道主题。

## 月度归档流程（仅每月 1 日执行）

1. 确定上个月：`YYYY-MM-prev`（例如今天是 2026-07-01，则处理 2026-06）。
2. 读取 `reports/YYYY-MM-prev.md`。
3. 基于整月内容，生成月度总结，需包含：
   - 本月 Top 5-8 重大事件
   - 3 条关键趋势
   - 高频公司/技术标签
   - 与上月的延续或变化
4. 将总结写入临时文件 `/tmp/ai-daily-summary-YYYY-MM-prev.md`。
5. 调用脚本归档：
   ```bash
   bash /Users/macmini/projects/cron/ai-daily/scripts/archive-month.sh YYYY-MM-prev /tmp/ai-daily-summary-YYYY-MM-prev.md
   ```
6. 脚本会自动：
   - 将总结插入到 `reports/YYYY-MM-prev.md` 最顶部
   - 生成 `reports/YYYY-MM-prev.html`
   - 同步 `.md` 和 `.html` 到 iCloud `数据同步/ai daily/`

## 每日日报流程

### 第一步：读取已报道主题

读取 `/Users/macmini/projects/cron/ai-daily/memory/ai-news-tracker.md`，获取最近 30 天已报道的主题列表。

### 第二步：数据采集

从以下 RSS 源获取今日（24 小时内）文章：

**国内源：**
| 来源 | URL |
|------|-----|
| 机器之心 | https://www.jiqizhixin.com/rss |
| InfoQ | https://www.infoq.cn/feed |
| Seebug Paper | https://paper.seebug.org/rss |

**海外源：**
| 来源 | URL |
|------|-----|
| TechCrunch | https://techcrunch.com/feed/ |
| The Verge | https://www.theverge.com/rss/index.xml |
| Ars Technica | https://feeds.arstechnica.com/arstechnica/index |
| OpenAI Blog | https://openai.com/news/rss.xml |

必要时使用 WebSearch 补充重要突发新闻。

**来源可信度要求：**
- 优先使用原始媒体或官方博客（TechCrunch、The Verge、机器之心、OpenAI Blog 等）。
- AI 聚合网站（如 buildfastwithai.com、aitoolsrecap.com）只能作为线索，关键事实需追溯到原始来源。
- 若无法验证真实性，标记为"据报道称"或降级为"其他要闻"。

### 第三步：去重筛选（关键）

**严格规则：**
- 如果新闻主题与 `ai-news-tracker.md` 中记录的主题高度相似（同一公司 + 同一事件线），**直接跳过**
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
| S级 | 重大技术突破、重磅产品发布、头部公司战略调整 | 必报，放 Breaking |
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
| **来源** | 每条注明来源 | `- 来源：TechCrunch` |

**内容结构：**
```markdown
### 🔥 Breaking

**🌍 新闻标题**
- **来源**：来源名 | **时间**：X月X日
- 要点 1
- 要点 2

---

**🌍 另一条 Breaking**
...

### 📌 核心动态
...

### 📎 其他要闻
...

### 💡 今日洞察

今日AI行业呈现X大趋势：
1. **趋势一**：详细阐述...
2. **趋势二**：详细阐述...
3. **趋势三**：详细阐述...
```

**每日精选 5-8 条，必须有 `### 💡 今日洞察` 段落。**

### 第六步：写入月报文件

1. 将生成的日报内容（不含日期标题）写入临时文件，例如 `/tmp/ai-daily-YYYY-MM-DD-body.md`。
2. 调用脚本追加到月报顶部：
   ```bash
   bash /Users/macmini/projects/cron/ai-daily/scripts/add-daily-entry.sh YYYY-MM-DD /tmp/ai-daily-YYYY-MM-DD-body.md
   ```
3. 脚本会自动：
   - 若 `reports/YYYY-MM.md` 不存在则创建
   - 在文件顶部插入 `## 【YYYY-MM-DD】` 和内容
   - 保持整月文件逆序

### 第七步：同步到 iCloud

调用脚本：
```bash
bash /Users/macmini/projects/cron/ai-daily/scripts/sync-to-icloud.sh YYYY-MM
```

脚本会：
1. 复制 `reports/YYYY-MM.md` 和 `reports/YYYY-MM.html` 到：
   ```
   ~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/
   ```
2. 更新 `index.html` 索引页。

### 第八步：更新追踪器

报道完成后，**必须**更新 `memory/ai-news-tracker.md`：

1. 添加今日日期和已报道主题（简洁格式）
2. 删除超过 30 天的旧记录
3. 主题格式：`公司-关键词-核心事实`（每行不超过 50 字符）

示例：
```markdown
## 2026-06-23

| 话题关键词 | 首次报道日期 | 简要描述 |
|-----------|-------------|---------|
| OpenAI-GPT5.5-发布 | 2026-06-23 | OpenAI发布GPT-5.5多模态大模型 |
| Google-Gemini-降价 | 2026-06-23 | Google将AI Plus降至$4.99 |
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
| 时间范围 | 只保留 24 小时内内容 |
| 数量控制 | 每日 5-8 条精华 |
| 去重 | 与 30 天内已报主题重合度 < 20% |
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

- 跟踪文件：`/Users/macmini/projects/cron/ai-daily/memory/ai-news-tracker.md`
- 月报文件：`/Users/macmini/projects/cron/ai-daily/reports/YYYY-MM.md`
- 可视化文件：`/Users/macmini/projects/cron/ai-daily/reports/YYYY-MM.html`
- iCloud 同步：`~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/`
- 执行日志：`/Users/macmini/projects/cron/ai-daily/logs/ai-daily-YYYYMMDD.log`
