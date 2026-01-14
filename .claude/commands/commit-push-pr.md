---
description: Commit changes and open a pull request
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(git branch:*), Bash(gh pr create:*)
---

# Context
- Current branch: !`git branch --show-current`
- Status: !`git status -sb`
- Diff summary: !`git diff --stat`

# Task
1. Review the changes above
2. Write a clear, conventional commit message following the format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `refactor:` for code refactoring
   - `test:` for tests
   - `chore:` for maintenance tasks
3. Stage all relevant changes
4. Commit with the prepared message
5. Push to origin
6. Create a pull request with:
   - A descriptive title
   - Summary of changes in the body
   - Any related issue references
