# 🔑 How to Enable GitHub Actions Workflow Automation

Your scheduled automation is ready, but your GitHub token needs the `workflow` scope to push workflow files.

## ⚠️ Current Issue
```
Personal Access Token missing 'workflow' scope
- Blocking: .github/workflows/auto-post-research-news.yml
- Status: Pending push to GitHub
```

## ✅ Solution: Update Your GitHub Token

### **Step 1: Create New Personal Access Token with Workflow Scope**

1. Go to GitHub Settings:
   - **GitHub.com** → Click your profile (top right)
   - Select **Settings**
   - Left sidebar: **Developer settings** → **Personal access tokens** → **Tokens (classic)**

2. Click **Generate new token** → **Generate new token (classic)**

3. Fill in the token details:
   ```
   Token name: github-actions-workflow
   Expiration: 90 days (recommended)
   ```

4. **Select these scopes:**
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
   - ✅ `read:user` (Read user profile data)
   - ✅ `public_repo` (Access public repositories)

5. Click **Generate token**

6. **Copy the token immediately** (you won't see it again!)
   - Format: `ghp_...`

### **Step 2: Update Your Local Git Configuration**

In PowerShell, replace the old token:

```powershell
# Option A: Update via command line
git remote set-url origin https://<NEW_TOKEN>@github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io.git

# Option B: Interactive (recommended)
# You'll be prompted for credentials next push
git config --global credential.helper manager
```

Replace `<NEW_TOKEN>` with the token you just created.

### **Step 3: Retry the Push**

```powershell
cd C:\Users\saifa\SaifaldeenALKADHIM.github.io
git push
```

Expected output:
```
Enumerating objects: 8, done.
...
To https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io.git
   6e7cf3d..73ee2d8  master -> master
✅ Success!
```

## 🚀 After Workflow is Pushed

Once the workflow is activated on GitHub:

### **View Your Workflow**
1. Go to your repository: https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io
2. Click **Actions** tab
3. Look for **"Auto-Post Research News"** workflow
4. Click it to see:
   - ✅ Scheduled runs
   - 📅 Next run date/time
   - 📋 Execution history
   - 📊 Logs from each run

### **First Scheduled Run**
- **Next:** Monday @ 9 AM UTC (or Thursday)
- **Or trigger manually:** Actions → Auto-Post Research News → Run workflow

### **Monitor Blog Posts**
- New posts appear in `_posts/` folder
- Blog updates at: https://SaifaldeenALKADHIM.github.io/year-archive/
- Each post tagged with: `#AI #Research #MEMS #Sensors`

## 📊 Workflow Schedule

```
📅 SCHEDULE: Monday & Thursday, 9 AM UTC

Mon Jan 20  → 9:00 AM UTC ⏰
Thu Jan 23  → 9:00 AM UTC ⏰
Mon Jan 27  → 9:00 AM UTC ⏰
...and so on
```

**Your timezone examples:**
- 🇺🇸 EST (New York): 4:00 AM
- 🇺🇸 PST (Los Angeles): 1:00 AM  
- 🇪🇺 CET (Budapest): 10:00 AM ✅
- 🇬🇧 GMT (London): 9:00 AM

## 🔒 Security Notes

- ✅ Token only used in GitHub Actions (not stored locally)
- ✅ Scoped to necessary permissions only
- ✅ Can revoke anytime from Settings
- ✅ Expires after 90 days (auto-rotate recommended)

## ❓ Troubleshooting

**Q: Token still not working?**
A: Delete old token, create fresh one, wait 5 minutes for GitHub to sync

**Q: How do I revoke the token?**
A: Settings → Developer settings → Personal access tokens → Delete (⚠️ workflow will stop)

**Q: Can I use a different expiration?**
A: Yes! Options: 7, 30, 60, 90 days, or No expiration (less secure)

---

**Files ready for activation:**
- ✅ `.github/workflows/auto-post-research-news.yml` (committed, awaiting push)
- ✅ `.github/scripts/fetch_research_news.py` (already pushed)
- ✅ `.github/AUTO_POST_README.md` (documentation)

**Once workflow is activated, your blog will auto-post research news every Monday & Thursday!** 🚀
