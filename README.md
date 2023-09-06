# Django Dashboard Application
# Introduction
This Django-based dashboard application allows users to manage to-do lists, check the weather for multiple locations, and set reminders with alert options.

# Prerequisites
Before running the application, ensure you have the following:

1.Python installed (Django is a Python web framework)
2.Django installed (pip install django)
3.API keys for any external services you are using (e.g., OpenWeatherMap)

# Installation
Clone the repository to your local machine:
Copy code
git clone https://github.com/safvan001/dashboardproject.git
cd dashboard_project
source venv/bin/activate  # On Windows, use venv\Scripts\activate
# Install project dependencies:
Run migrations to set up the database:
python manage.py migrate
Create a superuser to access the admin panel:
python manage.py createsuperuser
Start the development server:
python manage.py runserver
Open your web browser and navigate to http://localhost:8000 to access the dashboard.

# Usage
To-Do List
Navigate to the 'Todo List' page on the dashboard.

Use the interface to add, edit, or delete tasks in your to-do list.

# Weather
Go to the 'Weather' option on the dashboard.

The application should display weather information for the default locations or allow you to add and view weather for other locations.

# Reminders
Visit the 'Reminder' page on the dashboard.

Add reminders with a name and a selected time.

The application should display reminders.

Alert Options (Not Implemented Yet)
Note: Alert options for reminders are not implemented in the current version of the application due to time constraints.
