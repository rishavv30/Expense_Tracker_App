# Expense Tracker App

A simple and intuitive web application to track your daily expenses, manage your budget, and analyze spending patterns. Built with Django (Python) for the backend and HTML/CSS for the frontend.

---

## Features

- **User Authentication:** Secure login and registration system.
- **Add Expenses:** Quickly add daily expenses with details like amount, category, and date.
- **View Expenses:** Easily view all your past expenses in a structured format.
- **Edit & Delete:** Update or remove any expense entry.
- **Dashboard (Optional):** Visual representation of your spending trends (charts/graphs can be added).

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 
- **Database:** SQLite (default Django database)
- **Version Control:** Git & GitHub

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rishavv30/Expense_Tracker_App.git

2. Navigate to the project directory:
   cd Expense_Tracker_App

3. Create a virtual environment (recommended):
  python -m venv venv

Activate it:

On Windows: venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

4. Install dependencies:
  pip install -r requirements.txt
(If requirements.txt is missing, manually install Django: pip install django)

5. Apply migrations:
  python manage.py migrate

6. Run the development server:
  python manage.py runserver

Usage

Register a new account or login with existing credentials.
Navigate to the dashboard to add, edit, or delete expenses.
Track your spending over time and make informed budgeting decisions.
