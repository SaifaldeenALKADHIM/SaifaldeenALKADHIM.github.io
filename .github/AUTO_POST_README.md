# 🤖 Research News Auto-Post Agent

Automated blog posting system that fetches and publishes the latest research news related to AI, MEMS sensors, IoT, and your work.

## 📋 Features

- **Automatic Scheduling**: Runs every **Monday and Thursday at 9 AM UTC**
- **Intelligent Filtering**: Tracks 10+ research topics related to your work
- **Duplicate Prevention**: Won't create duplicate posts for the same research
- **arXiv Integration**: Fetches latest AI/ML papers from arXiv
- **RSS Feed Monitoring**: Collects relevant research from multiple feeds
- **Auto-Commit**: Automatically commits and pushes new posts to your blog

## 🎯 Tracked Research Topics

- AI Sensors
- MEMS Ionization Sensors
- IoT Systems with AI
- Carbon Nanotube Sensors
- Machine Learning on Edge Devices
- Neural Networks for Embedded Systems
- Hardware Acceleration for AI
- Smart Sensors & IoT Integration
- AI-driven Research
- Nanomaterial-based Sensors

## ⚙️ How It Works

### **Automatic Workflow**
```
Monday & Thursday @ 9 AM UTC
    ↓
Fetch latest research from:
  - arXiv AI/ML feeds
  - Research publication feeds
    ↓
Filter for relevant topics
    ↓
Create Jekyll blog posts
    ↓
Prevent duplicates
    ↓
Auto-commit & push to GitHub
    ↓
GitHub Pages rebuilds site
    ↓
Blog posts live at SaifaldeenALKADHIM.github.io
```

## 🚀 How to Use

### **View Scheduled Runs**
1. Go to your GitHub repository
2. Click **Actions** tab
3. Look for **"Auto-Post Research News"** workflow
4. See scheduled runs and execution logs

### **Manual Trigger**
You can manually trigger the workflow anytime:
1. Go to **Actions** → **Auto-Post Research News**
2. Click **Run workflow**
3. Select branch: `master`
4. Click **Run workflow**

### **Monitor Execution**
- Watch the **Actions** tab for real-time execution
- View logs to see what posts were created
- Check your blog at https://SaifaldeenALKADHIM.github.io/year-archive/ for new posts

## 📝 Generated Blog Post Format

Each auto-generated post includes:
```markdown
---
title: '📖 Research Brief: [Paper Title]'
date: 2026-01-16T19:44:25+01:00
permalink: /posts/YYYY-MM-DD-slug/
categories:
  - Research
tags:
  - AI
  - Research
  - arXiv
  - Machine Learning
excerpt: 'Latest research...'
---

**Authors:** [Author List]
**Published:** YYYY-MM-DD

## Summary
[Paper summary text]

## Read Full Paper
[Link to arXiv/Source]
```

## 🔧 Configuration

### **Change Schedule**
Edit `.github/workflows/auto-post-research-news.yml`:
```yaml
on:
  schedule:
    - cron: '0 9 * * 1,4'  # Monday (1) & Thursday (4)
```

**Cron Format:** `minute hour day month weekday`
- Every day: `'0 9 * * *'`
- Weekdays only: `'0 9 * * 1-5'`
- Specific time: `'30 14 * * 1'` (2:30 PM UTC Mondays)

### **Add Research Topics**
Edit `.github/scripts/fetch_research_news.py`:
```python
RESEARCH_TOPICS = [
    "your new topic",
    "another topic",
    # ... more topics
]
```

### **Change Post Limits**
In `fetch_research_news.py`, modify:
```python
papers[:3]   # Max papers per run
articles[:2] # Max articles per run
```

## 📊 What Gets Posted

The agent creates up to **5 posts per automated run**:
- **3 from arXiv** - Latest AI/ML papers
- **2 from RSS feeds** - Research news articles

To prevent your blog from being overwhelmed, the agent:
- Limits to max 5 posts per day
- Won't create duplicate posts for same research
- Tags all auto-posts with research categories
- Includes source attribution

## 🔗 Data Sources

### **arXiv Feeds** (Monitoring)
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning
- `eess.SY` - Systems and Control

### **RSS Feeds** (Research feeds)
Customizable list in `fetch_research_news.py`

## ✅ Success Indicators

✅ Workflow runs successfully
✅ New posts appear in `_posts/` folder
✅ Posts are automatically committed with timestamp
✅ GitHub Pages rebuild triggered
✅ New posts visible at `/year-archive/`

## ❌ Troubleshooting

| Issue | Solution |
|-------|----------|
| Workflow doesn't run | Check Actions tab for error logs |
| No posts created | Verify research topics match current publications |
| Duplicates appearing | Clear older posts or adjust filtering |
| Wrong publish time | Adjust cron schedule in workflow file |
| Posts not visible | Check GitHub Pages settings (master branch) |

## 📅 Schedule Options

| Frequency | Cron Expression |
|-----------|-----------------|
| Every day @ 9 AM | `0 9 * * *` |
| Mon & Thu @ 9 AM | `0 9 * * 1,4` |
| Weekdays @ 9 AM | `0 9 * * 1-5` |
| Every 6 hours | `0 */6 * * *` |
| Monthly 1st @ 9 AM | `0 9 1 * *` |

## 🎓 How It Helps Your Portfolio

1. **Fresh Content** - Blog automatically updates with latest research
2. **SEO Benefits** - Regular posts improve search rankings
3. **Engagement** - Shows active research awareness
4. **Time Saving** - No manual post creation needed
5. **Network Building** - Amplifies relevant research across your platform

## 📞 Support

If the workflow fails:
1. Check **Actions** tab → **Auto-Post Research News**
2. Review the error logs
3. Verify `.github/scripts/fetch_research_news.py` syntax
4. Check GitHub token permissions

---

**Created:** January 16, 2026  
**Next Run:** Monday 9 AM UTC (or manually via GitHub Actions)
