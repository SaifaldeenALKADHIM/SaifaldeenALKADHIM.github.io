# ☁️ GitHub Actions Cloud Automation Setup

**Enable Twice-Daily Auto-Posting that runs automatically even when your laptop is OFF**

---

## 🎯 What This Does

✅ Automatically posts research papers **2 times per day**
- 9 AM UTC (10 AM Budapest)
- 9 PM UTC (10 PM Budapest)

✅ **No computer needed** - runs on GitHub servers
✅ **Always on** - runs every single day
✅ **Laptop can be off** - completely cloud-based

---

## 🔑 Step 1: Update Your GitHub Token

Your current token doesn't have the `workflow` scope. You need to create a new one.

### Create New Token:

1. Go to: https://github.com/settings/tokens

2. Click **Generate new token** → **Tokens (classic)**

3. Fill in token details:
   ```
   Token name: github-actions-autopost
   Expiration: 90 days
   ```

4. **Select THESE scopes (copy exactly):**
   ```
   ✅ repo (Full control of private repositories)
   ✅ workflow (Update GitHub Action workflows) ← THIS IS REQUIRED
   ✅ read:user (Read user profile data)
   ✅ public_repo (Access public repositories)
   ```

5. Click **Generate token**

6. **COPY THE TOKEN** immediately (format: `ghp_...`)
   - ⚠️ You won't see it again!

---

## 💾 Step 2: Save Token Locally (Windows)

Open PowerShell and run:

```powershell
# Set your new token
$token = "ghp_PASTE_YOUR_TOKEN_HERE"

# Update git remote with token
git remote set-url origin "https://$($token)@github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io.git"

# Verify it worked
git remote -v
```

Replace `ghp_PASTE_YOUR_TOKEN_HERE` with your actual token!

---

## 🚀 Step 3: Push the Workflow

Now push the twice-daily automation:

```powershell
cd C:\Users\saifa\SaifaldeenALKADHIM.github.io

# Check status
git status

# Push everything
git push
```

**Expected output:**
```
Enumerating objects: X, done.
...
To https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io.git
   XXXXX..XXXXX  master -> master
✅ Success!
```

---

## ✅ Step 4: Verify Automation is Active

1. Go to your repo on GitHub.com:
   https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io

2. Click **Actions** tab

3. Look for **"Twice-Daily Auto-Post Research News"** workflow

4. You should see:
   ```
   ✅ Twice-Daily Auto-Post Research News
   📅 Scheduled for tomorrow 9 AM UTC
   ```

---

## 🕐 Schedule Timeline

**Your Automation Schedule (Budapest Time - CET/CEST):**

```
🕘 10:00 AM - Morning posts
   └─ 7+ research papers automatically posted
   └─ Auto-committed to GitHub
   └─ GitHub Pages rebuilds site

🕘 10:00 PM - Evening posts
   └─ 7+ more research papers
   └─ Auto-committed
   └─ Site updates live

📊 Result: 14 new posts daily!
```

---

## 📊 What to Expect

**First Run (Tomorrow Morning):**
- GitHub Actions executes at exactly 9 AM UTC
- Fetches latest arXiv papers
- Creates 7+ blog posts
- Auto-commits with timestamp
- Pushes to your blog
- GitHub Pages rebuilds (1-2 min)
- New posts visible on your website

**Ongoing:**
- Every day, twice per day
- Automatically, no interaction needed
- Even if your laptop is off
- Even if you're asleep
- Even if you're on vacation

---

## 🔍 Monitor Automation

**Check workflow runs:**
1. GitHub repo → **Actions** tab
2. Click **Twice-Daily Auto-Post Research News**
3. See all runs and logs
4. Green ✅ = successful
5. Red ❌ = check logs for errors

**Check new posts:**
1. Visit your blog: https://SaifaldeenALKADHIM.github.io/year-archive/
2. Look for latest posts with today's date
3. Should refresh after each run

**Check git commits:**
```powershell
git log --oneline | head -20
```

You'll see commits like:
```
✨ Auto-post: Research papers (2026-01-17 09:15 UTC)
✨ Auto-post: Research papers (2026-01-16 21:05 UTC)
```

---

## ⚙️ Customize Schedule (Optional)

Edit `.github/workflows/twice-daily-auto-post.yml` to change times:

```yaml
schedule:
  - cron: '0 8 * * *'   # 8 AM UTC instead of 9
  - cron: '0 20 * * *'  # 8 PM UTC instead of 9
```

**Other timezone examples:**
```yaml
# 7 AM & 7 PM UTC
- cron: '0 7 * * *'
- cron: '0 19 * * *'

# 6 AM & 6 PM UTC  
- cron: '0 6 * * *'
- cron: '0 18 * * *'
```

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Workflow doesn't appear in Actions** | Token doesn't have `workflow` scope - create new token |
| **Push fails with "permission denied"** | Token expired or wrong scope - generate new token |
| **No posts created** | Check Actions logs for arXiv API errors |
| **Posts not showing on blog** | Check GitHub Pages settings (1-2 min rebuild time) |
| **Git push error** | Run `git remote -v` to verify token in URL |

---

## 📋 Checklist

- [ ] Created new token with `workflow` scope
- [ ] Token has `ghp_` prefix
- [ ] Updated git remote with token
- [ ] Ran `git push` successfully
- [ ] Workflow file uploaded to GitHub
- [ ] Checked **Actions** tab - workflow visible
- [ ] Next scheduled time shows in workflow
- [ ] Waiting for first automated run...

---

## 🎉 You're Done!

Once token is set up and pushed:
- **✅ System is fully automated**
- **✅ Runs twice daily automatically**
- **✅ Works 24/7/365**
- **✅ No manual action needed**
- **✅ Laptop can always be off**

---

## 📞 Need Help?

**To manually trigger the workflow anytime:**
1. Go to GitHub repo → **Actions**
2. Click **Twice-Daily Auto-Post Research News**
3. Click **Run workflow**
4. Select **master** branch
5. Click **Run workflow**

Workflow runs immediately!

---

**Status:** Ready for cloud automation! ☁️🚀
