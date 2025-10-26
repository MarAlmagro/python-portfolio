# Django Delights 🍽️

Django Delights is a full-stack web application for restaurant inventory and sales management. It allows restaurant staff to track ingredient inventory, define menu items and their recipes, and record purchases in real-time. The application is designed for day-to-day operations with accurate stock management and real-time revenue reporting.

> Developed using Django 5.2 and Bootstrap 5.  
> Built for local development with SQLite; production-ready for PostgreSQL.

## 🧠 Project Summary

The owner of Django Delights needs a simple, efficient system to:

- Manage **ingredient inventory** (with price and quantity)
- Create **menu items** and define their required ingredients (recipes)
- **Track purchases** made by customers and update inventory accordingly
- Display key metrics: total inventory cost, daily revenue, purchase log, and restock needs

## 🧾 Features

✅ = Planned in initial version  
🕓 = To be implemented later

### Core Functionalities

- ✅ Ingredient management: name, quantity, price/unit  
- ✅ Menu item creation with price  
- ✅ Recipe definition: which ingredients are required for each menu item  
- ✅ Record customer purchases, update inventory  
- ✅ Prevent purchases that can't be fulfilled due to lack of ingredients  
- ✅ Timestamps for each purchase  
- ✅ Views for inventory, menu, recipe requirements, and purchase log  

### Metrics and Reports

- ✅ Total cost of current inventory  
- ✅ Total revenue for the day  
- ✅ List of purchases made  
- ✅ Inventory restock suggestions  

### User System

- ✅ Login/logout functionality  
- ✅ Views restricted to authenticated users  
- 🕓 Basic role-based permissions (optional)

## 🧱 Tech Stack

| Area             | Technology        |
|------------------|-------------------|
| Backend          | Django 5.2        |
| Database (dev)   | SQLite            |
| Database (prod)  | PostgreSQL (planned) |
| Frontend         | HTML, Bootstrap 5 |
| Environment Vars | python-dotenv     |
| Version Control  | Git + GitHub      |
| Dev Tools        | VS Code, CLI      |

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-delights.git
cd django-delights
```

### 2. Create Environment and Install Dependencies

```bash
python -m venv .venv
source .venv/Scripts/activate  # or .venv/bin/activate on Unix
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Edit .env with your settings.

### 4. Run Migrations and Start Server

```bash
python manage.py migrate
python manage.py runserver
```

## 🧪 Test User Login

You will need to create a superuser or use preloaded fixture users.

```bash
python manage.py createsuperuser
```

## 📁 Project Structure

```
django-delights/
├── config/            # Main Django project settings
├── delights/          # Core app: models, views, forms, etc.
├── templates/         # HTML templates (Bootstrap-based)
├── static/           # Static files (CSS, JS, etc.)
├── fixtures/         # Optional: sample data for development
├── .env              # Local environment variables
├── requirements.txt  # Python dependencies
└── README.md
```

## 📊 Future Enhancements

- PostgreSQL support for production  
- REST API endpoints (for future frontend or mobile clients)  
- Role-based permissions (e.g., Admin vs Staff)  
- Data export (CSV or PDF reports)

## 📄 License

This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).

## 🙌 Author

Built by [Mar Almagro](https://github.com/MarAlmagro) as part of a full-stack Django learning path.