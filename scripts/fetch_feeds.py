
import feedparser
import datetime

def fetch_all(feed_list):
    articles = []
    for url in feed_list:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "id": entry.get("id", entry.get("link","")),
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", str(datetime.datetime.utcnow()))
            })
    return articles
