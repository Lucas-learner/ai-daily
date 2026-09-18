#!/usr/bin/env python3
"""抓取 rss-feeds.txt 中固定源的近期条目，输出 JSONL 候选池（供日报子 agent 选用）。

用法：
  python3 scripts/fetch-rss.py [--hours N] [--feeds PATH] [--all]

  --hours N   只保留最近 N 小时内发布的条目（默认 25，覆盖日报 08:00-08:00 时间窗含余量）
  --feeds     源清单路径（默认 scripts/rss-feeds.txt）
  --all       不按时间过滤，输出全部解析到的条目

输出：stdout 每行一条 JSON：{"title","url","source","publishedAt"}
单个源失败只告警（stderr），不影响其他源。
网络策略：本机 Python(Homebrew 3.14) 的 TLS 握手会被服务端/中间层断开（curl 正常），
故抓取走 curl 子进程，顺序与 sync-to-github.sh 一致：先绕代理直连，再走默认代理。
仅依赖标准库 + curl，无需 feedparser。
"""

import argparse
import email.utils
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ATOM_NS = "{http://www.w3.org/2005/Atom}"
UA = "ai-daily-rss/1.0 (+https://lucas-learner.github.io/ai-daily/)"
TIMEOUT = 15


def load_feeds(path):
    feeds = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            continue
        name, url = (p.strip() for p in line.split("|", 1))
        if name and url:
            feeds.append((name, url))
    return feeds


def fetch(url):
    """先绕代理直连，失败则走默认代理（与 sync-to-github.sh 降级顺序一致）。返回 bytes。"""
    base = ["curl", "-fsSL", "-m", str(TIMEOUT), "-A", UA]
    try:
        return subprocess.run(
            [*base, "--noproxy", "*", url], check=True, capture_output=True
        ).stdout
    except subprocess.CalledProcessError:
        return subprocess.run([*base, url], check=True, capture_output=True).stdout


def parse_date(raw):
    """解析 RSS(RFC822) / Atom(ISO8601) 日期，返回 aware datetime 或 None。"""
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = email.utils.parsedate_to_datetime(raw)
        if dt:
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def text_of(el):
    return (el.text or "").strip() if el is not None else ""


def parse_feed(data):
    """返回 [{title, url, publishedAt}]，兼容 RSS 2.0 与 Atom。"""
    root = ET.fromstring(data)
    items = []

    if root.tag == f"{ATOM_NS}feed":  # Atom
        for entry in root.findall(f"{ATOM_NS}entry"):
            title = text_of(entry.find(f"{ATOM_NS}title"))
            link = ""
            for l in entry.findall(f"{ATOM_NS}link"):
                if l.get("href") and l.get("rel", "alternate") == "alternate":
                    link = l.get("href")
                    break
            date = text_of(entry.find(f"{ATOM_NS}published")) or text_of(
                entry.find(f"{ATOM_NS}updated")
            )
            items.append((title, link, date))
    else:  # RSS 2.0 / RDF
        for item in root.iter("item"):
            title = text_of(item.find("title"))
            link = text_of(item.find("link"))
            date = text_of(item.find("pubDate")) or text_of(
                item.find("{http://purl.org/dc/elements/1.1/}date")
            )
            items.append((title, link, date))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=25)
    ap.add_argument(
        "--feeds",
        default=str(Path(__file__).resolve().parent / "rss-feeds.txt"),
    )
    ap.add_argument("--all", action="store_true", help="不按时间过滤")
    args = ap.parse_args()

    cutoff = None if args.all else datetime.now(timezone.utc) - timedelta(
        hours=args.hours
    )

    seen = set()
    total = 0
    for name, url in load_feeds(args.feeds):
        try:
            entries = parse_feed(fetch(url))
        except Exception as e:  # noqa: BLE001 - 单源失败不阻塞整体
            print(f"WARN: {name} ({url}) 抓取失败: {e}", file=sys.stderr)
            continue
        kept = 0
        for title, link, date_raw in entries:
            if not title or not link or link in seen:
                continue
            dt = parse_date(date_raw)
            if cutoff and dt and dt < cutoff:
                continue
            seen.add(link)
            kept += 1
            total += 1
            print(
                json.dumps(
                    {
                        "title": title,
                        "url": link,
                        "source": name,
                        "publishedAt": dt.isoformat() if dt else None,
                    },
                    ensure_ascii=False,
                )
            )
        print(f"OK: {name} 候选 {kept} 条", file=sys.stderr)
    print(f"共 {total} 条候选", file=sys.stderr)


if __name__ == "__main__":
    main()
