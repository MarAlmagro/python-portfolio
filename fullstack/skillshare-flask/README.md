# Skillshare (Flask Version)

🧠 **What is Skillshare?**
Skillshare is a learning platform prototype where users register as students or mentors. It includes user authentication, session creation, and a simple interface to explore learning opportunities.

🌱 This is the **Flask version** of the Skillshare app. It focuses on building a monolithic structure using SQLite for development and PostgreSQL for production.

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

📁 **Directory Structure (Flask version):**
<pre lang="markdown"><code>
skillshare/ 
├── app/
│ ├── init.py
│ ├── models.py
│ ├── forms.py
│ ├── routes/
│ │ ├── init.py
│ │ └── auth_routes.py
│ ├── templates/
│ └── static/
├── tests/
├── .env
├── config.py
├── run.py
├── requirements.txt
└── README.md
</code></pre>


🧪 **Testing**

Use `pytest` or `unittest` depending on your setup:
``` bash
pytest tests/
```

🚀 **Run the project**
``` bash
flask run
```

🔐 **Environment Variables (.env)**
<pre lang="markdown"><code>
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///skillshare.db
</code></pre>

🔒 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for details.
