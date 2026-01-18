# Project Guidelines for Claude

## Project Overview
**Bhaisajyaguru (药师琉璃光如来)** - Online Buddhist temple static website.

## Tech Stack
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Hosting:** GitHub Pages (free, from `/docs` folder)
- **Site URL:** https://gz82.github.io/Bhaisajyaguru/

## Project Structure
```
Bhaisajyaguru/
├── docs/                    # Static site (GitHub Pages source)
│   ├── index.html           # Temple page
│   ├── scriptures.html      # Scriptures listing
│   ├── contacts.html        # Contact & donation
│   ├── scriptures/          # Individual sutra pages
│   ├── css/style.css
│   ├── js/temple.js
│   └── images/
├── documentation/           # Project docs (markdown)
├── backup/                  # Archived Flask app
└── .claude/commands/        # Claude Code slash commands
```

## Development
```bash
# Preview locally
cd docs && python -m http.server 8000
# Open http://localhost:8000

# Deploy: just push to main branch
git add . && git commit -m "feat: description" && git push
```

## Git Workflow
- Use conventional commits (feat:, fix:, docs:, refactor:)
- Do not include Co-Authored-By line in commits

## Notes
- GitHub Pages requires public repo (free)
- Custom domain supported (need to buy domain separately)
- Flask code archived in `/backup` for future use

---
*Update this file when conventions change.*
