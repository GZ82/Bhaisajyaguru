# Project Guidelines for Claude

## Project Overview
**Bhaisajyaguru** - A Flask web application for health/wellness remedies.

## Tech Stack
- **Language:** Python 3.10+
- **Framework:** Flask
- **Database:** SQLAlchemy (Flask-SQLAlchemy)
- **Authentication:** Flask-Login, Flask-Bcrypt
- **Forms:** Flask-WTF
- **API:** Flask-RESTful
- **Frontend:** Flask-Bootstrap, Jinja2 templates

## Development Workflow

### Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python run.py

# Run with gunicorn (production)
gunicorn run:app
```

### Project Structure
```
Bhaisajyaguru/
├── app/                  # Main application package
│   ├── routes/           # Blueprint routes
│   ├── templates/        # Jinja2 templates
│   ├── static/           # Static files (CSS, JS, images)
│   ├── models.py         # Database models
│   ├── forms.py          # WTForms
│   └── config.py         # Configuration
├── remedies/             # Legacy/alternative module
├── migrations/           # Database migrations
├── tests/                # Test suite
├── run.py                # Application entry point
└── requirements.txt      # Dependencies
```

## Style Guidelines
- Use snake_case for variables and functions
- Use PascalCase for class names
- Prefer explicit imports over wildcard imports
- Use type hints for function signatures
- Keep functions focused and under 50 lines
- Use docstrings for public functions and classes

## Flask Conventions
- Use Blueprints for route organization
- Use application factory pattern (`create_app()`)
- Store configuration in `config.py`, use environment variables for secrets
- Use Flask-Migrate for database schema changes

## Common Mistakes to Avoid
- Don't hardcode secrets or API keys - use environment variables
- Don't commit `.env` files or `instance/` folder
- Don't use `app.run()` in production - use gunicorn
- Don't forget to activate virtual environment before installing packages

## Testing
```bash
# Run tests (when configured)
pytest tests/
```

## Git Workflow
- Use conventional commits (feat:, fix:, docs:, refactor:, test:)
- Create feature branches from `main`
- Include issue/ticket numbers in commit messages when applicable

---
*This file is maintained by the team. Update it when Claude makes mistakes or when conventions change.*
