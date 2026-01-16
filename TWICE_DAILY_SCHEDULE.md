# 📅 Twice-Daily Auto-Post Schedule

This guide sets up automated research news posting **twice per day** to your blog.

## ⏰ Schedule Options

### **Option A: Windows Task Scheduler (Local)**
Run the Python script automatically every 12 hours on your Windows machine.

#### Setup Steps:

1. **Open Task Scheduler:**
   - Press `Win + R` → type `taskschd.msc` → Press Enter

2. **Create New Task:**
   - Right-click **Task Scheduler Library** → **Create Task**
   - Name: `Research News Auto-Post`
   - Check: ✅ Run with highest privileges

3. **Set Triggers (2 triggers for twice daily):**
   
   **Trigger 1 (Morning):**
   - Event: Begin a task
   - Type: On a schedule
   - Frequency: Daily
   - Start time: **9:00 AM**
   - Repeat every: 1 day
   
   **Trigger 2 (Evening):**
   - Event: Begin a task
   - Type: On a schedule
   - Frequency: Daily
   - Start time: **9:00 PM**
   - Repeat every: 1 day

4. **Set Action:**
   - Program: `C:\Users\saifa\AppData\Local\Programs\Python\Python313\python.exe`
   - Arguments: `.github/scripts/fetch_research_news.py`
   - Start in: `C:\Users\saifa\SaifaldeenALKADHIM.github.io`

5. **Set Conditions:**
   - ✅ Wake computer to run task
   - ✅ Run only if user is logged in

---

### **Option B: GitHub Actions (Cloud - After Token Update)**

Once your token has `workflow` scope, use twice-daily cron schedule:

```yaml
on:
  schedule:
    # 9 AM UTC (Morning)
    - cron: '0 9 * * *'
    # 9 PM UTC (Evening)
    - cron: '0 21 * * *'
```

This runs automatically without your computer being on.

---

## 📊 What Happens Each Run

**Per Each Execution:**
- ✅ Fetches 7 real arXiv papers
- ✅ Creates blog posts with authors and abstracts
- ✅ Auto-commits to git
- ✅ Pushes to GitHub
- ✅ GitHub Pages rebuilds

**Per Day:**
- 🕘 Morning (9 AM): 7 posts
- 🕘 Evening (9 PM): 7 posts
- **Total: 14 new research posts daily!**

---

## 🔧 Manual Trigger (Anytime)

Run immediately anytime:

```powershell
cd C:\Users\saifa\SaifaldeenALKADHIM.github.io
python .github/scripts/fetch_research_news.py
```

---

## 📱 Monitor Progress

1. **Check local folder:**
   ```powershell
   Get-ChildItem _posts/ | Sort-Object -Property LastWriteTime -Descending | Select-Object -First 5
   ```

2. **Check blog updates:**
   - Visit: https://SaifaldeenALKADHIM.github.io/year-archive/
   - Refresh every 5 minutes for latest posts

3. **Check git commits:**
   ```powershell
   git log --oneline | Select-Object -First 10
   ```

---

## ⚙️ Configuration

### Change Post Count Per Run
Edit `.github/scripts/fetch_research_news.py`:
```python
for paper in papers[:7]:  # Change 7 to your desired number
```

### Change Schedule Times
**Windows Task Scheduler:**
- Modify the triggers' start times (currently 9 AM & 9 PM)

**GitHub Actions (after token update):**
- Edit `.github/workflows/auto-post-research-news.yml`
- Change cron times:
  ```yaml
  - cron: '0 8 * * *'  # 8 AM UTC
  - cron: '0 20 * * *' # 8 PM UTC
  ```

### Timezone Conversion
Current schedule (UTC):
- 🕘 **9 AM UTC** → 10 AM Budapest (CET)
- 🕘 **9 PM UTC** → 10 PM Budapest (CET)

Other timezones:
- 🇺🇸 EST: 4 AM & 4 PM
- 🇺🇸 PST: 1 AM & 1 PM
- 🇪🇺 CET: 10 AM & 10 PM

---

## 📈 Expected Output

After 7 days with twice-daily posting:
- 📊 **98 new blog posts** (14 per day × 7 days)
- 📚 **Constantly updated research blog**
- 🔄 **Real-time AI & sensor technology tracking**
- 📱 **Fresh content for SEO & engagement**

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Posts not appearing | Check GitHub Pages rebuild (1-2 min) |
| Git push fails | Verify token has push permissions |
| Duplicate posts | Check `check_post_exists()` logic |
| Task Scheduler not running | Check Windows Event Viewer logs |
| No posts created | Verify arXiv API connectivity |

---

## 🎯 Next Steps

**Immediate (Local):**
1. Set up Windows Task Scheduler (Option A)
2. Test morning run manually
3. Verify posts appear on blog

**Future (Cloud - Recommended):**
1. Update GitHub token with `workflow` scope
2. Push `.github/workflows/auto-post-research-news.yml`
3. Let GitHub Actions handle the automation

---

**Status:** Ready for twice-daily posting! 🚀  
**Current Setup:** Manual + Windows Task Scheduler option available
