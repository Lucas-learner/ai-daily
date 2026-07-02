#!/bin/bash
set -euo pipefail

# 同步日报站点到 GitHub Pages
# 用法：sync-to-github.sh [YYYY-MM]
# 未指定月份时，默认同步本月及 docs/ 索引。

PROJECT_DIR="/Users/macmini/projects/skills/ai-daily"
REPO="Lucas-learner/ai-daily"

# 从 zshrc 提取 GITHUB_API_KEY（不 source 整个 zshrc，避免 bash 不兼容的补全脚本）
if [ -z "${GITHUB_API_KEY:-}" ] && [ -f "$HOME/.zshrc" ]; then
  GITHUB_API_KEY=$(grep -E '^[^#]*GITHUB_API_KEY=' "$HOME/.zshrc" | head -n1 | awk -F= '{print $2}' | tr -d '\"'"'"' ' | tr -d '[:space:]')
  export GITHUB_API_KEY
fi

if [ -z "${GITHUB_API_KEY:-}" ]; then
  echo "ERROR: GITHUB_API_KEY 未设置，无法 push 到 GitHub" >&2
  exit 1
fi

YEAR_MONTH="${1:-$(date +%Y-%m)}"

cd "$PROJECT_DIR"

# 1. 更新 docs/ 目录（HTML 报告 + 索引 + 摘要）
.venv/bin/python3 "$PROJECT_DIR/scripts/update-github-pages.py"

# 2. 提交变更（如果有）
if ! git diff --quiet -- docs/ scripts/update-github-pages.py scripts/generate-daily-summary.sh; then
  git add docs/ scripts/update-github-pages.py scripts/generate-daily-summary.sh
  git commit -m "chore: sync daily reports to GitHub Pages ($YEAR_MONTH)"
fi

# 3. push 到 GitHub（使用 token 避免交互式密码输入）
git push "https://${GITHUB_API_KEY}@github.com/${REPO}.git" main

echo "Synced GitHub Pages site for $YEAR_MONTH: https://${REPO%/*}.github.io/${REPO#*/}/"
