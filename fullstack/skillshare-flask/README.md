# Skillshare (Flask Version)

This project is part of a full-stack portfolio designed to showcase the evolution of a business logic idea across three Python frameworks: **Flask**, **FastAPI**, and **Django**.

🔧 **Current Stack:**
- Python 3.13+
- Flask
- SQLAlchemy
- Flask-Login
- Jinja2
- Bootstrap (via CDN)
- SQLite (dev) / PostgreSQL (prod)

🧩 **Main Features:**
- User authentication (register, login, logout)
- Role-based logic (e.g., students vs mentors)
- Forms with validation
- Jinja2 templating
- Bootstrap layout
- Error handling and logging
- Environment management (`python-dotenv`)
- Modular structure (`Blueprints`)
- Tests with `unittest` or `pytest`

🗃️ **Project Phases:**
1. Flask monolith (basic auth, MVC, SQLite)
2. FastAPI + PostgreSQL (API First design)
3. Django (monolith, TDD, admin)

📁 **Directory Structure (Flask version):**
skillshare/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── forms.py
│ ├── routes/
│ │ ├── init.py
│ │ └── auth_routes.py
│ ├── templates/
│ └── static/
│
├── tests/
├── .env
├── config.py
├── run.py
├── requirements.txt
└── README.md


🧪 **Testing**
Use `pytest` or `unittest` depending on your setup:
pytest tests/

🚀 **TRun the project**
flask run

🔐 **Environment Variables (.env)**
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///skillshare.db

🔒 **License**
This project is licensed under the MIT License. See the LICENSE
file for details.
