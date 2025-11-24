
def make_markdown(scored):
    lines = ["# Weekly Curated Feeds", ""]
    for item in sorted(scored, key=lambda x: -x["score"]):
        lines.append(f"## {item['title']}")
        lines.append(f"- **Score:** {item['score']}")
        lines.append(f"- **Link:** {item['link']}")
        lines.append(f"- **Tags:** {', '.join(item['tags'])}")
        lines.append(f"- **Why:** {item['justification']}")
        lines.append("")
    return "\n".join(lines)
