# Ariayi Team Website

A Django-based company landing page with dynamic content management, built as a learning project to practice backend web development with Django.

## Features

- Dynamic project showcase powered by Django models and querysets
- Contact form with CSRF protection, saved to the database
- Django admin panel for managing site content (projects, footer info, contact messages)
- RTL Persian layout with a custom dark theme
- Responsive design (mobile, tablet, desktop)

## Tech Stack

- **Backend:** Django 6.0, Python 3.13
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap (RTL), custom CSS, vanilla JavaScript

## Project Structure

```
├── projects_app/       # Project showcase model, views
├── contactus_app/      # Footer info and contact message models
├── templates/          # HTML templates
├── assets/             # Static source files (CSS, JS, images, fonts)
└── manage.py
```

## Installation

```bash
git clone https://github.com/Beirami/ariayi-team-website.git
cd ariayi-team-website
python -m venv .venv
.venv\Scripts\activate  
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   #for admin access
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Note on the Frontend

The HTML/CSS frontend template was adapted from an existing Bootstrap-based template rather than built from scratch. I customized it with a new color scheme (Persian Green), a dark theme, updated branding, and fixed several existing bugs (broken modal markup, invalid form handling). All backend functionality — models, views, forms, and admin configuration — was built independently.

## What I Learned

- Structuring a multi-app Django project (separate apps for projects and contact/footer content)
- Using Django's ORM and querysets to render dynamic content in templates
- Handling POST form submissions securely with CSRF protection
- Customizing the Django admin panel for non-technical content management
- Debugging environment issues (virtualenv paths, project renaming, static files)

## Author

**Ahoora Beirami**
GitHub: [@Beirami](https://github.com/Beirami)