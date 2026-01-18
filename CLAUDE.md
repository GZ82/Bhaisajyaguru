# Project Guidelines for Claude

## Project Overview
**Bhaisajyaguru (药师琉璃光如来)** - Online Buddhist temple static website.

## Development Workflow
**Static site in `/docs` folder, deployed via GitHub Pages.**

## Commands
1. Preview locally: `cd docs && python -m http.server 8000`
2. Deploy: `git add . && git commit -m "feat: description" && git push`

## Style Guidelines
- Use semantic HTML5 elements
- Keep CSS in `/docs/css/style.css`
- Use vanilla JavaScript only — no frameworks
- Mobile-first responsive design

## Architecture Decisions
- Static site in `/docs` — GitHub Pages source
- Documentation in `/documentation` — markdown files
- Flask code archived in `/backup` — for future dynamic features
- External services for donations, analytics — via hyperlinks

## Common Mistakes to Avoid
- Don't add Co-Authored-By line in commits
- Don't use relative paths starting with `/` — use `./` or `../`
- Don't commit large media files — optimize images first

## Git Guidelines
- Use conventional commits (feat:, fix:, docs:, refactor:)
- Push to `main` branch to deploy

## Project URLs
- **Site:** https://gz82.github.io/Bhaisajyaguru/
- **Repo:** https://github.com/GZ82/Bhaisajyaguru
