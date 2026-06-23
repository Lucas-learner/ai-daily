# AI日报（cron + kimi-code 版）

原 OpenClaw 的 `ai-daily` skill 迁移至此，改为使用 kimi-code 的 `CronCreate` 定时激发。

## 目录

```
.
├── .kimi-code/skills/ai-daily/SKILL.md   # 日报执行 skill
├── AGENTS.md                             # 项目级 Agent 指令
├── memory/
│   └── ai-news-tracker.md               # 去重追踪器
├── reports/
│   └── YYYY-MM.md                       # 每月日报汇总
├── logs/
│   └── ai-daily-YYYYMMDD.log            # 执行日志
└── scripts/
    ├── add-daily-entry.sh               # 将日报追加到月文件顶部
    ├── archive-month.sh                 # 月度总结 + HTML + iCloud 同步
    └── md-to-html.py                    # Markdown 转 HTML
```

## 定时任务

- 时间：每天 08:00（Asia/Shanghai）
- 方式：kimi-code `CronCreate`
- Prompt：调用项目级 `ai-daily` skill

## iCloud 同步

每月 `.md` 与渲染后的 `.html` 会同步到：

```
~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/
```

## 历史数据

历史日报已从 `/Users/macmini/OpenClawWorkspace/memory/` 迁移并按月份合并到 `reports/`。
原始 OpenClaw 文件保留不变。
