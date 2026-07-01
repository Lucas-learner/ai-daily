# AI日报（cron + kimi-code 版）

使用 kimi-code 的 `CronCreate` 定时生成 AI 行业日报。

> 🌐 **公开日报站点**：https://lucas-learner.github.io/ai-daily/

## 目录

```
.
├── .kimi-code/skills/ai-daily/SKILL.md   # 日报执行 skill（唯一事实来源）
├── .venv/                                # Python 虚拟环境（markdown 渲染）
├── AGENTS.md                             # 项目级 Agent 指令
├── README.md                             # 本文件
├── docs/                                 # GitHub Pages 站点源文件
│   ├── index.html                        # 公开日报索引页
│   ├── daily-summary.html                # 最新日报摘要
│   └── reports/                          # 可视化日报 HTML
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
    ├── cron-run.sh                      # 系统 cron 入口
    ├── generate-daily-summary.sh        # 生成每日摘要（支持 iCloud/GitHub 输出目录）
    ├── md-to-html.py                    # Markdown 转 HTML
    ├── sync-to-icloud.sh                # 同步到 iCloud
    ├── sync-to-github.sh                # 同步到 GitHub Pages
    ├── update-icloud-index.py           # 更新 iCloud 索引页
    └── update-github-pages.py           # 更新 GitHub Pages 索引页
```

## 定时任务

- 时间：每天 08:07（Asia/Shanghai）
- 方式：系统级 `crontab`（生产兜底）
  - 入口脚本：`scripts/cron-run.sh`
  - 命令：`kimi -p "执行ai日报任务"`
  - 同步目标：iCloud + GitHub Pages（每日自动更新）
- 备用方式：kimi-code 内置 `CronCreate`（仅当前 session 生效，7 天后过期）

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

## Skill 维护

项目级 skill 是单一事实来源：

```
/Users/macmini/projects/skills/ai-daily/.kimi-code/skills/ai-daily/SKILL.md
```

用户级 skill 是符号链接：

```
/Users/macmini/.kimi-code/skills/ai-daily/SKILL.md
```

修改项目级文件即可，无需手动同步。
