# Copilot Instructions for Academic Portfolio Website

## Project Overview
Personal academic portfolio built with **Jekyll + Minimal Mistakes theme**, auto-deployed via **GitHub Pages** (`master` branch). Showcases publications, conference talks, teaching materials, projects, and blog posts.

**Tech Stack:** Jekyll (github-pages gem), Ruby/Bundler, Node.js/npm, Python (content generators)  
**Live Site:** `https://SaifaldeenALKADHIM.github.io`

---

## Architecture Overview

### Directory Structure
```
├── _config.yml              # Main site configuration
├── _config.dev.yml          # Development overrides
├── _data/                   # Data files (navigation, UI text)
├── _includes/               # Reusable HTML partials
├── _layouts/                # Page templates
├── _sass/                   # SASS stylesheets
├── _pages/                  # Static pages (About, CV, etc.)
├── _publications/           # Research papers (collection)
├── _talks/                  # Conference talks (collection)
├── _teaching/               # Teaching materials (collection)
├── _portfolio/              # Project showcases (collection)
├── _posts/                  # Blog posts (YYYY-MM-DD-*.md)
├── _drafts/                 # Unpublished posts
├── markdown_generator/      # Python/TSV bulk content tools
├── images/                  # Image assets
├── files/                   # Downloadable files
└── assets/js/               # JavaScript (built to main.min.js)
```

### Jekyll Collections
Collections organize academic content with structured frontmatter:

**Publications** (`_publications/*.md`):
```yaml
title: "Paper Title"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
date: 2009-10-01
venue: 'Journal/Conference Name'
paperurl: 'http://link-to-paper.pdf'
citation: 'Author. (Year). "Title." <i>Venue</i>.'
excerpt: 'Brief description'
```

**Talks** (`_talks/*.md`):
```yaml
title: "Talk Title"
collection: talks
type: "Conference/Tutorial"
permalink: /talks/2017-04-05-tutorial-1
venue: "Conference Name"
date: 2017-04-05
location: "City, Country"
```

**Posts** (`_posts/YYYY-MM-DD-*.md`):
```yaml
title: 'Post Title'
date: 2022-02-02
permalink: /posts/2022-02-02-post/
tags:
  - Tag1
  - Tag2
```

### Configuration Hierarchy
- **`_config.yml`**: Author profile, site metadata, collection settings, analytics, theme defaults
- **`_config.dev.yml`**: Development-only overrides (merged with `--config _config.yml,_config.dev.yml`)
- **`_data/navigation.yml`**: Top navigation menu links
- **Layout defaults**: Defined in `_config.yml` under `defaults:` (avoid repeating in individual files)

---

## Development Workflow

### Local Development Setup
```bash
# First-time setup
bundle install              # Install Ruby dependencies
npm install                 # Install Node.js dependencies

# Start development server
bundle exec jekyll serve    # http://localhost:4000

# Development mode (shows drafts, uses _config.dev.yml)
bundle exec jekyll serve --config _config.yml,_config.dev.yml --drafts
```

**Critical:** Always use `bundle exec jekyll serve` (never bare `jekyll serve`) to match GitHub Pages gem versions.

**Auto-rebuild:** Content changes reload automatically, but `_config.yml` edits require server restart.

### JavaScript Build Process
```bash
npm run build:js            # Uglify & concatenate to assets/js/main.min.js
npm run watch:js            # Watch mode for active development
```

Built file includes: jQuery, fitvids, greedy-navigation, magnific-popup, smooth-scroll, stickyfill.

---

## Content Management

### Bulk Content Generation (Preferred Method)
Use Python scripts in `markdown_generator/` for publications/talks at scale:

**1. Edit TSV files:**
- `markdown_generator/publications.tsv`: pub_date, title, venue, excerpt, citation, url_slug, paper_url
- `markdown_generator/talks.tsv`: date, title, type, location, venue, url_slug

**2. Generate Markdown:**
```bash
python markdown_generator/publications.py  # → _publications/YYYY-MM-DD-*.md
python markdown_generator/talks.py         # → _talks/YYYY-MM-DD-*.md
```

**Requirements:** pandas, geopy, getorg

### Manual Content Creation
Copy existing files as templates, update frontmatter. File naming convention:
- **Publications/Talks:** `YYYY-MM-DD-url-slug.md` (date-prefixed, matches permalink)
- **Posts:** `YYYY-MM-DD-title-slug.md` (Jekyll standard)
- **Pages:** `name.md` (no date prefix)

### Geographic Talk Visualization
Generate interactive map from talk locations:
```bash
cd _talks
python ../talkmap.py        # → ../talkmap/index.html
```
Geocodes `location:` fields from talk frontmatter using Nominatim.

---

## Site Configuration

### Author Profile Management
Edit `author:` section in `_config.yml`:
```yaml
author:
  name: "Full Name"
  avatar: "profile.png"           # From images/ directory
  bio: "Short bio text"
  location: "City, Country"
  email: "email@example.com"
  googlescholar: "https://..."
  researchgate: "https://..."
  # ... other social links
```
Changes appear in sidebar across all pages.

### Navigation Menu
Edit `_data/navigation.yml`:
```yaml
main:
  - title: "Publications"
    url: /publications/
  - title: "Custom Page"
    url: /custom-page/
```

### Analytics & SEO
In `_config.yml`:
```yaml
google_site_verification: "verification-code"
analytics:
  provider: "google-universal"
  google:
    tracking_id: "UA-XXXXXXXX"
```

### Collection Defaults
Defined in `_config.yml` under `defaults:` - **DO NOT repeat** in individual files:
- **Publications:** `layout: single`, `author_profile: true`, `share: true`, `comments: true`
- **Talks:** `layout: talk`, `author_profile: true`, `share: true`
- **Posts:** `layout: single`, `read_time: true`, `related: true`

---

## File Conventions

### Permalinks
- **Collections:** `/:collection/:path/` (path = filename without extension)
- **Posts:** `/:categories/:title/`
- **Override:** Set explicit `permalink:` in frontmatter

### Images & Assets
```markdown
![Alt text](/images/filename.png)      # Store in /images/ or /files/
```
Profile picture: `author.avatar` in `_config.yml` → `images/profile.png`

### Draft Posts
Place in `_drafts/` (no date prefix). View locally: `bundle exec jekyll serve --drafts`

---

## Deployment & Dependencies

### Automatic Deployment
- **Trigger:** Push to `master` branch
- **Platform:** GitHub Pages (builds Jekyll automatically)
- **No action required:** Site rebuilds on commit

### Dependencies
- **Jekyll:** Controlled by `github-pages` gem (DO NOT specify separate Jekyll version)
- **Theme:** Minimal Mistakes (integrated via theme framework)
- **Jekyll Plugins:** jekyll-feed, jekyll-sitemap, hawkins (live reload), jekyll-redirect-from
- **Python Tools:** pandas (TSV processing), geopy/getorg (geocoding)
- **Node.js:** uglify-js, onchange (JS minification/watching)

### Allowed Jekyll Plugins
Only plugins in `github-pages` gem whitelist work in production. Check whitelist before adding new plugins.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Changes not appearing locally | Restart Jekyll server after `_config.yml` edits |
| Build failure on GitHub | Check repo Settings → Pages for build log |
| Plugin not working in production | Verify plugin is in github-pages gem whitelist |
| Broken permalinks | Ensure frontmatter permalink matches filename pattern |
| JavaScript changes ignored | Run `npm run build:js` to regenerate main.min.js |
| Missing navigation items | Check `_data/navigation.yml` syntax and indentation |

---

## Project-Specific Notes

### Nested Repository
`SaifaldeenALKADHIM.github.io/` subdirectory is a duplicate nested repo - should be removed or clarified.

### MATLAB Section
Custom collection for MATLAB-related content (see `_MATLAB/` and navigation item).
