
# RSS Curator Agent

This tool fetches articles from RSS feeds, scores them using vector embeddings and tag-based interest learning, and generates a weekly markdown digest.

## Features
- Weekly GitHub Actions automation
- Embedding-based relevance scoring
- Tag-based interest system that learns from article content
- Per-week cache of seen articles (auto-clears on each run)
- Markdown output suitable for Obsidian

## Installation
```bash
pip install -r requirements.txt
```

Create a `.env` or set:
```
OPENAI_API_KEY=your_key
```

Run:
```bash
python scripts/run_all.py
```

## GitHub Actions
Add your `OPENAI_API_KEY` as a repository secret.
