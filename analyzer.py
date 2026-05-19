#!/usr/bin/env python3
"""GitHub Repo Analyzer - Find contribution opportunities."""

import argparse
import json
import sys
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.parse import urlencode

GITHUB_API = "https://api.github.com"


def api_request(endpoint, params=None):
    """Make a GitHub API request."""
    url = f"{GITHUB_API}{endpoint}"
    if params:
        url += "?" + urlencode(params)
    req = Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "github-repo-analyzer")
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def search_issues(label="good first issue", language=None, days=30):
    """Search for issues with given label."""
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    query = f'label:"{label}" state:open created:>{since}'
    if language:
        query += f" language:{language}"
    
    data = api_request("/search/issues", {"q": query, "sort": "created", "order": "desc", "per_page": 10})
    if not data:
        return []
    
    issues = []
    for item in data.get("items", [])[:10]:
        repo_url = item.get("repository_url", "")
        parts = repo_url.split("/")
        repo = f"{parts[-2]}/{parts[-1]}" if len(parts) >= 2 else "unknown"
        issues.append({
            "repo": repo,
            "number": item.get("number"),
            "title": item.get("title", "")[:60],
            "url": item.get("html_url"),
        })
    return issues


def main():
    parser = argparse.ArgumentParser(description="GitHub Repo Analyzer")
    subparsers = parser.add_subparsers(dest="command")
    
    search_parser = subparsers.add_parser("search", help="Search for issues")
    search_parser.add_argument("--label", default="good first issue", help="Issue label")
    search_parser.add_argument("--language", help="Programming language")
    search_parser.add_argument("--days", type=int, default=30, help="Days since creation")
    
    args = parser.parse_args()
    
    if args.command == "search":
        issues = search_issues(args.label, args.language, args.days)
        if issues:
            print(f"\nFound {len(issues)} issues:\n")
            for issue in issues:
                print(f"  {issue['repo']} | #{issue['number']} | {issue['title']}")
                print(f"    → {issue['url']}\n")
        else:
            print("No issues found.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
