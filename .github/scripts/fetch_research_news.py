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

def fetch_arxiv_papers(query, max_results=5):
    """Fetch latest papers from arXiv related to research topics"""
    try:
        base_url = "http://export.arxiv.org/api/query?"
        search_query = f"cat:cs.AI OR cat:cs.LG OR cat:eess.SY"
        url = f"{base_url}search_query={search_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        papers = []
        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.content)
        
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            published = entry.find('{http://www.w3.org/2005/Atom}published').text
            arxiv_id = entry.find('{http://www.w3.org/2005/Atom}id').text.split('/abs/')[-1]
            authors = [author.find('{http://www.w3.org/2005/Atom}name').text 
                      for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
            
            # Check if paper is relevant
            full_text = (title + " " + summary).lower()
            if any(topic.lower() in full_text for topic in RESEARCH_TOPICS):
                papers.append({
                    'title': title,
                    'summary': summary.strip(),
                    'published': published,
                    'arxiv_id': arxiv_id,
                    'authors': authors,
                    'url': f"https://arxiv.org/abs/{arxiv_id}"
                })
        
        return papers
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
    
    for post_file in posts_dir.glob("*.md"):
        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if title in content:
                return True
    return False

def create_blog_post(title, content, tags=None):
    """Create a new blog post in Jekyll format"""
    if tags is None:
        tags = ["AI", "Research", "MEMS", "Sensors", "IoT"]
    
    # Check if post already exists
    if check_post_exists(title):
        print(f"Post '{title}' already exists. Skipping.")
        return False
    
    # Create filename
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:50]
    filename = f"_posts/{date_str}-{slug}.md"
    
    # Check if filename already exists today
    posts_dir = Path("_posts")
    if posts_dir.exists():
        existing = list(posts_dir.glob(f"{date_str}-*.md"))
        if len(existing) > 5:  # Limit 5 posts per day
            print(f"Already created {len(existing)} posts today. Skipping.")
            return False
    
    # Create post frontmatter
    frontmatter = f"""---
title: '{title}'
date: {today.isoformat()}
permalink: /posts/{date_str}-{slug}/
categories:
  - Research
tags:
  - {chr(10).join(f'  - {tag}' for tag in tags)}
excerpt: 'Latest research and news related to AI, MEMS sensors, and IoT systems'
---

{content}
"""
    
    # Write post
    posts_dir.mkdir(parents=True, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    print(f"✅ Created post: {filename}")
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
    for paper in papers[:3]:  # Limit to 3 posts per run
        title = f"📖 Research Brief: {paper['title'][:60]}"
        
        content = f"""
**Authors:** {', '.join(paper['authors'][:3])}

**Published:** {paper['published'][:10]}

## Summary
{paper['summary'][:300]}...

## Read Full Paper
[View on arXiv]({paper['url']})

**Keywords:** AI, Machine Learning, Research, Sensors, IoT

---
*This is an auto-generated post from latest research publications related to your work.*
"""
        
        if create_blog_post(title, content, tags=["AI", "Research", "arXiv", "Machine Learning"]):
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
    print(f"🚀 Ready to commit and push!")

if __name__ == "__main__":
    main()
