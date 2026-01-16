#!/usr/bin/env python3
"""
Auto-post research news agent for blog
Fetches latest AI, MEMS, IoT, and sensor research from multiple sources
"""

import os
import json
import requests
import feedparser
from datetime import datetime, timedelta
from pathlib import Path
import re

# Research topics related to Saifaldeen's work
RESEARCH_TOPICS = [
    "AI sensors",
    "MEMS ionization sensor",
    "IoT systems AI",
    "carbon nanotube sensors",
    "machine learning edge computing",
    "neural networks embedded systems",
    "AI hardware acceleration",
    "nanomaterial sensors",
    "smart sensors",
    "AI-driven IoT"
]

# RSS Feeds for research news
RSS_FEEDS = [
    "https://feeds.arxiv.org/rss/cs.AI",  # Artificial Intelligence
    "https://feeds.arxiv.org/rss/cs.LG",  # Machine Learning
    "https://feeds.arxiv.org/rss/eess.SY",  # Systems and Control
]

def fetch_arxiv_papers(query, max_results=10):
    """Fetch latest papers from arXiv using multiple keyword searches"""
    try:
        base_url = "http://export.arxiv.org/api/query?"
        papers = []
        import xml.etree.ElementTree as ET
        
        # Search for papers with keywords related to research
        search_queries = [
            "all:MEMS AND all:sensor",
            "all:machine learning AND all:IoT",
            "all:carbon nanotube AND all:sensor",
            "all:neural network AND all:embedded",
            "all:edge computing AND all:AI"
        ]
        
        for search_query in search_queries:
            try:
                url = f"{base_url}search_query={search_query}&sortBy=submittedDate&sortOrder=descending&max_results=5"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                root = ET.fromstring(response.content)
                
                for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                    title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                    summary_elem = entry.find('{http://www.w3.org/2005/Atom}summary')
                    published_elem = entry.find('{http://www.w3.org/2005/Atom}published')
                    id_elem = entry.find('{http://www.w3.org/2005/Atom}id')
                    
                    if all([title_elem is not None, summary_elem is not None, 
                           published_elem is not None, id_elem is not None]):
                        
                        title = title_elem.text.strip()
                        summary = summary_elem.text.strip()
                        published = published_elem.text[:10]
                        arxiv_id = id_elem.text.split('/abs/')[-1]
                        
                        authors = []
                        for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
                            name_elem = author.find('{http://www.w3.org/2005/Atom}name')
                            if name_elem is not None:
                                authors.append(name_elem.text)
                        
                        paper = {
                            'title': title,
                            'summary': summary[:300],
                            'published': published,
                            'arxiv_id': arxiv_id,
                            'authors': authors[:5],  # Limit to 5 authors
                            'url': f"https://arxiv.org/abs/{arxiv_id}"
                        }
                        
                        # Avoid duplicates
                        if not any(p['arxiv_id'] == arxiv_id for p in papers):
                            papers.append(paper)
            except Exception as e:
                print(f"  ⚠️ Error with query '{search_query}': {e}")
                continue
        
        return papers[:max_results]
    except Exception as e:
        print(f"Error fetching arXiv papers: {e}")
        return []

def fetch_rss_news(max_items=10):
    """Fetch latest news from research RSS feeds"""
    articles = []
    
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:max_items]:
                title = entry.get('title', 'No title')
                summary = entry.get('summary', '')
                published = entry.get('published', datetime.now().isoformat())
                link = entry.get('link', '')
                
                # Check if relevant to research
                full_text = (title + " " + summary).lower()
                if any(topic.lower() in full_text for topic in RESEARCH_TOPICS):
                    articles.append({
                        'title': title,
                        'summary': summary[:500],
                        'published': published,
                        'link': link,
                        'source': feed.feed.get('title', 'Research Feed')
                    })
        except Exception as e:
            print(f"Error fetching RSS feed {feed_url}: {e}")
    
    return articles

def check_post_exists(title):
    """Check if a post with this title already exists"""
    posts_dir = Path("_posts")
    if not posts_dir.exists():
        return False
    
    # Extract core title (remove emojis and extra text)
    core_title = re.sub(r'[^a-z0-9\s]', '', title.lower())
    core_title_short = ' '.join(core_title.split()[:5])  # First 5 words
    
    for post_file in posts_dir.glob("*.md"):
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                # Check if significant portion of title is already in posts
                if core_title_short in content:
                    return True
        except:
            pass
    return False

def create_blog_post(title, content, tags=None):
    """Create a new blog post in Jekyll format"""
    if tags is None:
        tags = ["AI", "Research", "MEMS", "Sensors", "IoT"]
    
    # Check if post already exists
    if check_post_exists(title):
        print(f"  ℹ️  Post with similar title exists. Skipping.")
        return False
    
    # Use PAST date so Jekyll displays it immediately
    today = datetime.now()
    past_date = today - timedelta(days=1)  # Yesterday's date ensures it's always in the past
    date_str = past_date.strftime("%Y-%m-%d")
    date_iso = past_date.isoformat()
    
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:60]
    filename = f"_posts/{date_str}-{slug}.md"
    
    # Check if filename already exists today
    posts_dir = Path("_posts")
    if posts_dir.exists():
        existing = list(posts_dir.glob(f"{date_str}-*.md"))
        if len(existing) > 15:  # Increased to 15 posts per day (for twice daily posting)
            print(f"  ⚠️  Already created {len(existing)} posts today (limit reached).")
            return False
    
    # Create post frontmatter with proper YAML formatting
    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)
    
    frontmatter = f"""---
title: '{title.replace("'", "\\\"")}'
date: {date_iso}
permalink: /posts/{date_str}-{slug}/
categories:
  - Research
tags:
{tags_yaml}
excerpt: 'Latest research on AI, MEMS sensors, IoT systems, and emerging technologies'
---

{content}
"""
    
    # Write post
    posts_dir.mkdir(parents=True, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    print(f"✅ Created: {filename}")
    return True

def main():
    print("🤖 Research News Auto-Post Agent Started")
    print(f"⏰ Time: {datetime.now().isoformat()}")
    print(f"🔍 Tracking: {', '.join(RESEARCH_TOPICS[:5])}...\n")
    
    # Fetch papers from arXiv
    print("📚 Fetching from arXiv...")
    papers = fetch_arxiv_papers("research papers", max_results=10)
    
    posts_created = 0
    
    # Create posts from papers
    for paper in papers[:7]:  # 7 posts per run (supports twice daily)
        title = f"📖 {paper['title'][:70]}"
        
        authors_str = ', '.join(paper['authors'][:5]) if paper['authors'] else 'Unknown Authors'
        
        content = f"""**Authors:** {authors_str}

**Published:** {paper['published']}

**arXiv ID:** {paper['arxiv_id']}

## Summary

{paper['summary']}

## Research Connection

This paper relates to current advances in:
- Machine Learning and AI systems
- Embedded computing and edge devices
- Sensor networks and IoT
- Neural networks and optimization

## Read Full Paper

[View on arXiv]({paper['url']})

---
*Auto-posted from arXiv latest research. {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*
"""
        
        if create_blog_post(title, content, tags=["AI", "Research", "arXiv", "ML", "IoT"]):
            posts_created += 1
    
    # Fetch and create from RSS feeds
    print("\n🌐 Fetching from Research Feeds...")
    articles = fetch_rss_news(max_items=5)
    
    for article in articles[:2]:  # Limit to 2 posts from feeds
        title = f"📰 {article['title'][:60]}"
        
        content = f"""
**Source:** {article['source']}

**Published:** {article['published'][:10]}

## Overview
{article['summary'][:300]}...

[Read Full Article]({article['link']})

**Related to:** AI, Research, MEMS, Sensors, IoT

---
*This is an auto-generated post from research news feeds.*
"""
        
        if create_blog_post(title, content, tags=["News", "Research", "AI", "Technology"]):
            posts_created += 1
    
    print(f"\n✨ Auto-Post Summary")
    print(f"📝 Posts created: {posts_created}")
    print(f"⏰ Next run: Twice daily (Morning & Evening)")
    print(f"🚀 Ready to commit and push!")

if __name__ == "__main__":
    main()
