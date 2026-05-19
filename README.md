# GitHub Repo Analyzer

A simple CLI tool to analyze GitHub repositories and find contribution opportunities.

## Features

- Search for repos with "good first issue" labels
- Find documentation fixes
- Identify trending projects
- Filter by language, stars, and activity

## Installation

```bash
pip install github-repo-analyzer
```

## Usage

```bash
# Find good first issues in Python repos
gha search --language python --label "good first issue"

# Find documentation fixes
g ha docs --min-stars 1000

# Analyze a specific repo
g ha analyze owner/repo
```

## Support

If this tool helps you, consider supporting development:

**ETH:** `0xE1854bE3A859F1B9B40814d9711E7d5d2cFE9C80`

## License

MIT
