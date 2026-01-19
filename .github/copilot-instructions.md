# Copilot Instructions for Academic Portfolio Website

## Project Overview
Personal academic portfolio built with **Jekyll + Minimal Mistakes theme**, auto-deployed via **GitHub Pages** (`master` branch). Showcases publications, conference talks, teaching materials, projects, and blog posts for MEMS/IoT research.

**Tech Stack:** Jekyll (github-pages gem), Ruby/Bundler, Node.js/npm, Python (content generators & automation)  
**Live Site:** `https://SaifaldeenALKADHIM.github.io`

---

## Architecture Overview

### Core Directory Structure
```
├── _config.yml              # Main site configuration (author, collections, defaults)
├── _config.dev.yml          # Dev overrides (use with --config flag)
├── _data/navigation.yml     # Top menu links
├── _includes/               # HTML partials (analytics, sidebar, etc.)
├── _layouts/                # Page templates (single, talk, archive)
├── _sass/                   # SASS stylesheets
├── _pages/                  # Static pages (About, CV, etc.)
├── _publications/           # Research papers (YYYY-MM-DD-slug.md)
├── _talks/                  # Conference talks (YYYY-MM-DD-slug.md)
├── _teaching/               # Teaching materials
├── _portfolio/              # Project showcases
├── _posts/                  # Blog posts (YYYY-MM-DD-*.md) - FLAT structure
├── _drafts/                 # Unpublished posts (no date prefix)
├── .github/
│   ├── workflows/           # auto-post-research-news.yml
│   └── scripts/             # fetch_research_news.py
├── markdown_generator/      # Python TSV→Markdown converters
│   ├── publications.py      # TSV to _publications/*.md
│   ├── talks.py             # TSV to _talks/*.md
│   └── *.tsv                # Bulk import data
├── images/                  # Image assets
├── files/                   # Downloadable PDFs, etc.
└── assets/js/               # JS source (builds to main.min.js)
```

### Jekyll Collections (Academic Content Organization)
All collections use **date-prefixed filenames** (`YYYY-MM-DD-slug.md`) and structured frontmatter:

**Publications** (`_publications/2025-01-19-ionization-sensor.md`):
```yaml
title: "Paper Title"
collection: publications
permalink: /publication/2025-01-19-paper-slug
date: 2025-01-19
venue: 'Sensors and Actuators A: Physical'
paperurl: 'https://doi.org/10.1016/...'
citation: 'Alkadhim, S. et al. (2025). "Title." <i>Journal</i>.'
excerpt: 'Brief description for listing pages'
```

**Talks** (`_talks/2024-06-15-conference-talk.md`):
```yaml
title: "Talk Title"
collection: talks
type: "Conference/Tutorial/Invited"
permalink: /talks/2024-06-15-talk-slug
venue: "IEEE Conference Name"
date: 2024-06-15
location: "Budapest, Hungary"
```

**Posts** (`_posts/2026-01-19-research-topic.md`):
- **Critical:** Posts MUST be in flat `_posts/` directory (no subdirectories)
- Jekyll ignores posts in nested folders like `_posts/2026/`
- Use tags/categories for organization, NOT folder structure
```yaml
title: 'Post Title'
date: 2026-01-19
permalink: /posts/2026-01-19-post-slug/
tags:
  - AI
  - MEMS
  - IoT
```

### Configuration Hierarchy & Defaults
**`_config.yml` (lines 160-200)** defines layout defaults for all collections:
```yaml
defaults:
  - scope: {path: "", type: posts}
    values: {layout: single, author_profile: true, read_time: true, comments: true, share: true}
  - scope: {path: "", type: publications}
    values: {layout: single, author_profile: true, share: true, comments: true}
  - scope: {path: "", type: talks}
    values: {layout: talk, author_profile: true, share: true}
```
**Never duplicate these in individual .md files** - inheritance is automatic.

**`_data/navigation.yml`**: Defines main menu links (About, Research, Blog, Teaching, Talks, Portfolio, CV).

---

## Development Workflow

### Local Development Commands
```bash
# First-time setup
bundle install              # Ruby gems (Jekyll, github-pages)
npm install                 # Node.js tools (uglify-js, onchange)

# Standard development server
bundle exec jekyll serve    # http://localhost:4000, auto-rebuild

# Development mode (show drafts, use dev config)
bundle exec jekyll serve --config _config.yml,_config.dev.yml --drafts

# Live reload (requires hawkins gem)
bundle exec jekyll serve --livereload
```

**Critical Rules:**
- Always use `bundle exec jekyll serve` (never bare `jekyll serve`)
- Restart server after editing `_config.yml` (config changes not auto-reloaded)
- Content/layout changes rebuild automatically
- Posts in nested folders won't appear (Jekyll bug) - keep flat `_posts/`

### JavaScript Build Process
```bash
npm run build:js            # Uglify & concat → assets/js/main.min.js
npm run watch:js            # Watch mode for active JS development
```
Bundles: jQuery, fitvids, greedy-navigation, magnific-popup, smooth-scroll, stickyfill.

### Python Environment (Optional)
If using markdown generators or automation scripts:
```bash
# Using virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate    # Unix
pip install pandas feedparser requests python-dateutil geopy getorg
```

---

## Content Management Workflows

### Bulk Publications/Talks Import (Preferred)
Use Python TSV converters in `markdown_generator/` for batch imports:

**1. Edit TSV files:**
- `publications.tsv`: pub_date, title, venue, excerpt, citation, url_slug, paper_url
- `talks.tsv`: date, title, type, location, venue, url_slug

**2. Generate Markdown:**
```bash
cd markdown_generator
python publications.py      # → ../_publications/YYYY-MM-DD-*.md
python talks.py             # → ../_talks/YYYY-MM-DD-*.md
```

**3. Verify & Commit:**
Check generated files have proper frontmatter, then `git add` and commit.

**Script Details:**
- `publications.py` (109 lines): Reads TSV, escapes YAML special chars (`&`, `"`, `'`), writes markdown with metadata + download links
- Uses pandas for TSV parsing
- HTML-escapes venues/citations to prevent YAML breakage

### Manual Content Creation
Copy existing file as template:
```bash
# Publications/Talks (date-prefixed)
cp _publications/2025-01-19-example.md _publications/2026-02-01-new-paper.md

# Blog posts (must be flat in _posts/)
cp _posts/2026-01-19-example.md _posts/2026-02-15-new-post.md

# Pages (no date prefix)
cp _pages/about.md _pages/new-page.md
```
Update frontmatter `title`, `date`, `permalink`, `url_slug` to match new filename.

### Automated Blog Posting (Research News Agent)
GitHub Actions workflow `.github/workflows/auto-post-research-news.yml`:
- **Schedule:** Monday & Thursday at 9 AM UTC (`cron: '0 9 * * 1,4'`)
- **Script:** `.github/scripts/fetch_research_news.py` (430 lines)
- **Sources:** arXiv feeds (AI, ML, Systems), Nature, IEEE Xplore
- **Topics:** AI sensors, MEMS, IoT, carbon nanotubes, edge computing, semiconductors
- **Output:** Creates blog posts in `_posts/` with YAML frontmatter + content
- **Deduplication:** Checks existing posts to prevent duplicates
- **Auto-commit:** Pushes to `master` if new posts generated

**Manual Trigger:** Run from GitHub Actions tab → "Auto-Post Research News" → "Run workflow"

### Geographic Talk Map Generation
```bash
cd _talks
python ../talkmap.py        # → ../talkmap/index.html
```
- Geocodes `location:` fields from talk frontmatter using Nominatim
- Generates interactive map of conference/talk locations
- Requires: geopy, getorg

---

## Site Configuration

### Author Profile (`_config.yml` lines 46-89)
```yaml
author:
  name: "Saif Aldeen Saad Obayes Al-Kadhim, Ph.D."
  avatar: "profile.png"     # → images/profile.png
  bio: "Assistant Professor | IEEE Senior Member | MEMS & IoT Expert"
  location: "Budapest, Hungary"
  email: "saifaldeen.saad@ieee.org"
  googlescholar: "https://scholar.google.com/citations?user=..."
  researchgate: "https://www.researchgate.net/profile/..."
  linkedin: "saif-aldeen-al-kadhim-96230561"
  orcid: "http://orcid.org/0000-0002-2082-9591"
  github: "SaifaldeenALKADHIM"
  twitter: "saifoony"
```
Profile appears in sidebar on all pages. Update `avatar` filename if changing profile image.

### Navigation Menu (`_data/navigation.yml`)
```yaml
main:
  - title: "About"
    url: /
  - title: "Research"
    url: /publications/
  - title: "Blog"
    url: /year-archive/
```
Order matters - appears left-to-right in top menu.

### SEO & Analytics (`_config.yml` lines 16-43)
```yaml
google_site_verification: "4TZ5HtV-5XZR7qxoxfJIXeBg3ymdmPytFzH08pHKKI0"
analytics:
  provider: "google-universal"
  google:
    tracking_id: "UA-XXXXXXXX"
twitter:
  username: "saifoony"
og_image: # Open Graph image for social sharing
```

---

## File Conventions & Critical Rules

### Blog Post Structure (CRITICAL)
**DO:**
- Place posts directly in `_posts/` (flat structure)
- Name: `YYYY-MM-DD-descriptive-slug.md`
- Use tags for categorization, not folders

**DON'T:**
- Create subdirectories like `_posts/2026/` (Jekyll ignores nested posts)
- Use categories in folder structure (breaks Jekyll build)

### Permalinks
- **Collections:** `/:collection/:path/` (path = filename without `.md`)
- **Posts:** `/:categories/:title/` or explicit `permalink:` in frontmatter
- **Slug Rule:** Filename slug MUST match permalink slug for predictable URLs

### Images & Assets
```markdown
![Alt text](/images/filename.png)      # Absolute path from site root
[Download PDF](/files/paper.pdf)       # Files directory for downloads
```
- Profile picture: `images/profile.png` (referenced in `_config.yml`)
- No need for `{{ site.baseurl }}` - GitHub Pages handles this

### Drafts
- Place in `_drafts/` with no date prefix: `draft-post-title.md`
- View locally: `bundle exec jekyll serve --drafts`
- Publish: Move to `_posts/` and add date prefix

---

## Deployment & CI/CD

### Automatic Deployment
- **Trigger:** Push to `master` branch
- **Platform:** GitHub Pages (auto-builds Jekyll)
- **Build Time:** ~1-2 minutes after push
- **Check Build:** Repo Settings → Pages → Build log

### GitHub Actions Workflows
1. **auto-post-research-news.yml**: Bi-weekly research news automation (see above)
2. **Future workflows**: Add to `.github/workflows/` (must have proper permissions)

### Dependencies Management
**Ruby (Gemfile):**
- `github-pages` gem (locks Jekyll/plugin versions)
- Never specify Jekyll version separately (conflicts with github-pages)
- Plugins: jekyll-feed, jekyll-sitemap, hawkins (livereload), jekyll-redirect-from

**Node.js (package.json):**
- uglify-js, onchange (JS build tools)
- Minimal Mistakes theme v3.4.2

**Python (requirements.txt if created):**
- pandas (TSV processing)
- feedparser, requests, python-dateutil (auto-post script)
- geopy, getorg (geocoding for talkmap)

**Jekyll Plugin Whitelist:**
Only these plugins work on GitHub Pages: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed, jemoji, jekyll-redirect-from. Don't add unlisted plugins.

---

## Troubleshooting Common Issues

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Posts not appearing | Nested in `_posts/2026/` subdirectories | Move to flat `_posts/` structure |
| Changes not showing locally | `_config.yml` edited | Restart Jekyll server (Ctrl+C, re-run `bundle exec jekyll serve`) |
| Build fails on GitHub | Invalid YAML frontmatter | Check for unescaped special chars (`&`, `"`, `'`) in titles/citations |
| Plugin not working in prod | Plugin not in whitelist | Check `_config.yml` whitelist, remove unlisted plugins |
| JS changes ignored | Forgot to rebuild | Run `npm run build:js` to regenerate `main.min.js` |
| Broken author profile | Wrong image path | Verify `images/profile.png` exists, check `author.avatar` in `_config.yml` |
| Navigation menu missing | YAML syntax error | Validate `_data/navigation.yml` indentation |
| Permalink 404 | Filename/permalink mismatch | Ensure `permalink:` matches `YYYY-MM-DD-slug` pattern |

---

## Project-Specific Notes

### Custom Collections
- **MATLAB**: `_MATLAB/` for MATLAB-related content (navigation item configured)
- **Comsol**: `Comsol/` directory for COMSOL Multiphysics simulation files

### Research Focus Areas (for AI agents creating content)
When generating posts/publications, relevant keywords:
- MEMS ionization sensors, carbon nanotube sensors, aerosol detection
- IoT systems, edge computing, smart sensors
- Machine learning on embedded devices, neural networks for hardware
- Battery safety monitoring, gas sensing technologies
- IEEE standards (P2418.11), automotive applications
