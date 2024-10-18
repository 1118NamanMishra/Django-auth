Django Authentication App

This is a simple Django-based authentication application where users can register, log in, view the home page, and log out.
It implements basic user authentication and session management.

## Features
- User registration
- User login
- Protected home page (only accessible after login)
- User logout

## Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Django Templates

## Prerequisites
- Python 3.x
- Django 3.x or higher
- Git (optional for cloning the repository)

## Installation
1. Clone the repository
git clone https://github.com/yourusername/Django-auth.git
cd Django-auth

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

If `requirements.txt` doesn't exist, use this command instead:
pip install django

4. Apply migrations
python manage.py migrate

5. Create a superuser (optional, for accessing the admin panel)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver
Visit `http://127.0.0.1:8000/` in your web browser.

## Usage
# Registration
- Navigate to `/register/` to create a new account.
- Enter your username, password, and other required details.

# Login
- Navigate to `/login/` to log in.
- After successful login, you will be redirected to the home page.

# Home Page
- The home page is protected and can only be accessed by logged-in users.
- If not logged in, you will be redirected to the login page.

# Logout
- You can log out by clicking the logout button on the home page.
- After logging out, you will be redirected to the login page.
