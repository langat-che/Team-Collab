
# Team-Collab
A Team Collaboration and Productivity software
This repository contains the source code for the **Team Collaboration** Django application, designed to help teams manage their tasks and facilitate efficient collaboration.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Features](#features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Prerequisites
Ensure you have the following installed on your machine before proceeding:

1. **Python (>=3.8)**: [Download Python](https://www.python.org/downloads/)
2. **Pip**: Python package installer (comes with Python)
3. **Git**: [Download Git](https://git-scm.com/)
4. **Virtualenv** (optional but recommended): Install it via pip: `pip install virtualenv`
5. **Database (optional)**: Depending on the database used (e.g., PostgreSQL, MySQL), ensure it is installed and configured.

---

## Installation
Follow these steps to clone and set up the project:

1. **Clone the Repository**
   ```bash
   cd your-project-folder
   git clone https://github.com/langat-che/Team-Collab.git
   cd Team-Collab
   ```

2. **Set Up a Virtual Environment**
   Create and activate a virtual environment (optional but recommended):

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment (Linux/Mac)
   source venv/bin/activate

   # Activate virtual environment (Windows)
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   Use pip to install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root and set up environment variables (if applicable).     Example:

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # Replace with your database connection string if using another database
   ```

5. **Apply Migrations**
   Run database migrations to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
---

## Running the Application
Start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.(ctrl + click-on-link)

---

## Features
- Manage cases, clients, tasks, and deadlines.
- Dynamic filters and search functionality.
- Calendar integration for task deadlines.
- Role-based access control.

---

## Troubleshooting
- If you encounter database errors, ensure the database server is running and the connection settings are correct.
- For missing dependencies, run `pip install -r requirements.txt` again.

---

## Contributing
Contributions are welcomed! Please fork this repository and submit a pull request.

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request.

---
