Travello - Django Web Application
==================================

Overview
--------
Travello is a Django-based web application built with modular apps such as accounts, calc, and travello. 
It implements core Django concepts like models, views, templates, static files, user authentication, and database management (SQLite).

This project is structured to support a scalable, multi-app Django environment.

Features
--------
- User Authentication (Login / Registration)
- Basic Calculator App (calc)
- Travel Listings (travello app)
- Organized static and media file management
- Admin Dashboard (using Django’s admin panel)

Project Structure
-----------------
projects/proj_1/
│
├── accounts/            # User authentication system
├── assets/admin/        # Admin-specific static assets
├── calc/                # Calculator mini-app
├── media/images/        # Uploaded media files
├── proj_1/              # Project configuration files (settings.py, urls.py)
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── travello/            # Travel-related features
├── db.sqlite3           # Default Django database
└── manage.py            # Django management script

Setup Instructions
------------------
1. Clone the Repository
   git clone https://github.com/Suryakausthub/Django---Backend/
   cd projects/proj_1

2. Create a Virtual Environment
   python -m venv venv
   source venv/bin/activate    (On Windows: venv\Scripts\activate)

3. Install Dependencies
   pip install django

4. Run Migrations
   python manage.py makemigrations
   python manage.py migrate

5. Run the Development Server
   python manage.py runserver

6. Access the App
   Open your browser and go to http://127.0.0.1:8000/

Tech Stack
----------
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap (inside templates/ and static/)
- Database: SQLite (default)

Acknowledgments
---------------
- Django Documentation
- Bootstrap Framework
- Free-to-use travel images for UI development

Contact
-------
If you face any issues or want to contribute, feel free to raise an issue or submit a pull request!
