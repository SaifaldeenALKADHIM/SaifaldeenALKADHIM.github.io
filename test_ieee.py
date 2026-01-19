#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, '.github/scripts')
from fetch_research_news import fetch_ieee_xplore

# Test IEEE Xplore
print("Testing IEEE Xplore fetch...\n")
articles = fetch_ieee_xplore()

print(f"\n✅ Total IEEE articles: {len(articles)}\n")
for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(f"   Link: {article['link']}")
    print(f"   Summary: {article['summary'][:100]}...")
    print()
