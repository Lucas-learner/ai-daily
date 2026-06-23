# AI日报（cron + kimi-code 版）

原 OpenClaw 的 `ai-daily` skill 迁移至此，改为使用 kimi-code 的 `CronCreate` 定时激发。

## 目录

```
.
├── .kimi-code/skills/ai-daily/SKILL.md   # 日报执行 skill（唯一事实来源）
├── .venv/                                # Python 虚拟环境（markdown 渲染）
├── AGENTS.md                             # 项目级 Agent 指令
├── README.md                             # 本文件
├── memory/
│   └── ai-news-tracker.md               # 去重追踪器
├── reports/
│   ├── YYYY-MM.md                       # 每月日报汇总
│   └── YYYY-MM.html                     # 可视化版本（由脚本生成）
├── logs/
│   └── ai-daily-YYYYMMDD.log            # 执行日志
└── scripts/
    ├── add-daily-entry.sh               # 将日报追加到月文件顶部
    ├── archive-month.sh                 # 月度总结 + HTML + iCloud 同步
    ├── md-to-html.py                    # Markdown 转 HTML
    ├── sync-to-icloud.sh                # 同步到 iCloud
    └── update-icloud-index.py           # 更新 iCloud 索引页
```

## 定时任务

- 时间：每天 08:00（Asia/Shanghai）
- 方式：kimi-code `CronCreate`
- Prompt：调用 `ai-daily` skill（同时存在于项目级和用户级，用户级为符号链接）

## iCloud 同步

每月 `.md`、渲染后的 `.html` 以及 `index.html` 索引页会同步到：

```
~/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily/
```

## 依赖

```bash
python3 -m venv .venv
.venv/bin/pip install markdown
```

## Git

项目已初始化 git。修改后建议提交：

```bash
git add .
git commit -m "描述"
```

## 历史数据

历史日报已从 `/Users/macmini/OpenClawWorkspace/memory/` 迁移并按月份合并到 `reports/`。
原始 OpenClaw 文件保留不变。

## Skill 维护

项目级 skill 是单一事实来源：

```
/Users/macmini/projects/cron/ai-daily/.kimi-code/skills/ai-daily/SKILL.md
```

用户级 skill 是符号链接：

```
/Users/macmini/.kimi-code/skills/ai-daily/SKILL.md
```

修改项目级文件即可，无需手动同步。
