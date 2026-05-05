# Makrly.io Website Previews

Static hosting for website preview files using GitHub Pages.

## URL Structure

```
https://makrly.io/client-name/project-name/
```

## Current Previews

| Client | Project | URL |
|--------|---------|-----|
| liberty-roofing | refresh-v2 | https://makrly.io/liberty-roofing-refresh-v2/ |

## Adding a New Preview

1. Create a new folder: `/client-name/project-name/`
2. Add your `index.html` and all related files (CSS, JS, images)
3. Commit and push to GitHub
4. The preview will be live at `https://makrly.io/client-name/project-name/`

### Example

```bash
mkdir -p new-client/new-project
cp -r your-website-files/* new-client/new-project/
git add .
git commit -m "Add preview for new-client/new-project"
git push origin main
```

## Folder Structure

```
makrly.github.io/
├── README.md
├── liberty-roofing-refresh-v2/
│   └── index.html
├── client-name/
│   └── project-name/
│       ├── index.html
│       ├── css/
│       ├── js/
│       └── images/
└── ...
```

## Important Notes

- All files are public - don't include sensitive data
- Use relative paths for assets: `./css/style.css` or `images/logo.png`
- GitHub Pages may take 1-2 minutes to update after pushing
- The repository name `makrly.github.io` creates the root domain (no `/repo-name/` in the URL)

## DNS Setup (for makrly.io domain)

To connect the custom domain `makrly.io`:

### 1. Add CNAME file to repo

Create a file named `CNAME` in the root:
```
makrly.io
```

### 2. Configure DNS at your registrar

Add these DNS records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | makrly.github.io |

### 3. Enable in GitHub

1. Go to repository Settings → Pages
2. Under "Custom domain", enter: `makrly.io`
3. Check "Enforce HTTPS" once DNS propagates

### Verification

After DNS propagates (can take up to 24 hours), visit:
- https://makrly.io/liberty-roofing-refresh-v2/

---

**Repository:** https://github.com/brettswensen/makrly.github.ioBuild attempt Mon May  4 17:55:05 MDT 2026
# Force rebuild 1777948099
