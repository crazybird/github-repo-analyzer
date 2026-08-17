# 🔍 GitHub Repo Analyzer

[![Stars](https://img.shields.io/github/stars/crazybird/github-repo-analyzer?style=social)](https://github.com/crazybird/github-repo-analyzer)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Find your next open source contribution in seconds, not hours.

Tired of scrolling through GitHub trying to find beginner-friendly issues? This tool automatically searches, filters, and ranks "good first issues" across thousands of repositories.

## ✨ Features

- 🔎 **Smart Search** - Find issues by language, label, and date range
- 📊 **Difficulty Rating** - Auto-classifies issues as Easy/Medium/Hard
- 📄 **Markdown Reports** - Generate shareable reports
- ⚡ **GitHub Action** - Automated weekly scans
- 🎯 **Beginner Friendly** - Perfect for first-time contributors

## 🚀 Quick Start

### Installation

Make sure Python 3.8 or newer is installed. Then install the project using:

```bash
pip install -e .
```

After installation, you can use the `gha` command to analyze GitHub repositories.

### CLI

```bash
# Find easy Python issues from last week
python analyzer.py search --language python --days 7

# Generate a markdown report
python analyzer.py search --language javascript --days 14 --output report.md
```

### GitHub Action

```yaml
name: Weekly Issue Scan
on:
  schedule:
    - cron: '0 9 * * 1'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: crazybird/github-repo-analyzer@v1
        with:
          language: 'python'
          days: '7'
```

## 📸 Example Output

```
🟢 Easy | Dev-TechT/local-llm-searxng-agent#3
  Add documented Ollama example for OpenAI-compatible local endpoint
  → https://github.com/Dev-TechT/local-llm-searxng-agent/issues/3

🟡 Medium | traoreera/xcore#219
  Commande CLI `xcore migration` pour piloter `MigrationRunner`
  → https://github.com/traoreera/xcore/issues/219
```

See [examples/sample-report.md](examples/sample-report.md) for a full report.

## 💝 Support

If this tool helped you find your first open source contribution:

**ETH:** `0xE1854bE3A859F1B9B40814d9711E7d5d2cFE9C80`

Your support helps maintain and improve this tool for the community.

## 📄 License

MIT © Open Source Contributor
