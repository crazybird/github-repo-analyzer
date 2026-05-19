# 🔍 GitHub Repo Analyzer

Find GitHub contribution opportunities automatically.

## Features

- 🔎 Search for "good first issues" across repositories
- 📅 Filter by language, date range, and labels
- ⚡ GitHub Action for automated weekly scans
- 📊 Perfect for maintainers and new contributors

## Quick Start

### CLI Usage

```bash
# Find good first issues in Python repos
python analyzer.py search --language python --days 7

# Find documentation fixes
python analyzer.py search --label documentation --days 30
```

### GitHub Action

```yaml
- uses: crazybird/github-repo-analyzer@v1
  with:
    language: 'python'
    days: '7'
```

## Support

If this tool helps you find your next contribution, consider supporting development:

**ETH:** `0xE1854bE3A859F1B9B40814d9711E7d5d2cFE9C80`

## License

MIT
