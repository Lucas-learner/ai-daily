#!/usr/bin/env python3
"""
通过 GitHub Contents API 直接更新仓库文件，作为 git push 失败时的兜底方案。
仅更新 docs/ 目录下用于 GitHub Pages 的文件。
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

PROJECT_DIR = "/Users/macmini/projects/skills/ai-daily"
REPO = "Lucas-learner/ai-daily"
BRANCH = "main"


def get_token():
    with open(os.path.expanduser("~/.zshrc")) as f:
        for line in f:
            m = re.match(r'^\s*GITHUB_API_KEY\s*=\s*["\']?(.*?)["\']?\s*$', line)
            if m:
                return m.group(1).strip().strip('"').strip("'")
    raise RuntimeError("GITHUB_API_KEY not found in ~/.zshrc")


def api_request(path, method="GET", data=None, token=None):
    url = f"https://api.github.com/repos/{REPO}{path}"
    headers = {
        "User-Agent": "ai-daily",
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
        payload = json.dumps(data).encode("utf-8")
    else:
        payload = None
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return e.code, json.loads(body) if body else {"message": str(e)}


def get_sha(path, token):
    status, data = api_request(f"/contents/{path}?ref={BRANCH}", token=token)
    if status == 200:
        return data.get("sha")
    if status == 404:
        return None
    raise RuntimeError(f"Failed to get SHA for {path}: {status} {data}")


def update_file(repo_path, local_path, message, token):
    with open(local_path, "rb") as f:
        content = f.read()
    encoded = base64.b64encode(content).decode("utf-8")
    sha = get_sha(repo_path, token)
    data = {
        "message": message,
        "content": encoded,
        "branch": BRANCH,
    }
    if sha:
        data["sha"] = sha
    status, resp = api_request(f"/contents/{repo_path}", method="PUT", data=data, token=token)
    if status not in (200, 201):
        raise RuntimeError(f"Failed to update {repo_path}: {status} {resp}")
    print(f"Updated {repo_path}")


def main():
    token = get_token()
    files_to_push = []
    docs_dir = os.path.join(PROJECT_DIR, "docs")
    for root, _, files in os.walk(docs_dir):
        for name in files:
            local_path = os.path.join(root, name)
            rel_path = os.path.relpath(local_path, docs_dir)
            repo_path = f"docs/{rel_path}"
            files_to_push.append((repo_path, local_path))

    message = f"chore: sync GitHub Pages via API ({os.path.basename(__file__)})"
    for repo_path, local_path in sorted(files_to_push):
        try:
            update_file(repo_path, local_path, message, token)
        except Exception as e:
            print(f"ERROR updating {repo_path}: {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
