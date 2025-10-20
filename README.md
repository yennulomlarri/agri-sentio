🌾 Agri-Sentio Backend API
Crop Disease Detection & Farm Analytics Platform

📘 Overview
Agri-Sentio is an AI-powered crop disease detection and farm management platform. This backend system is built with Django REST Framework and integrates TensorFlow for intelligent crop disease classification.

It provides secure user authentication, farm management, diagnostic analysis, taxonomy data, and admin analytics dashboards.

🧩 Features
Module	Description
Accounts	Custom user model with JWT authentication (SimpleJWT)
Farms	Register, manage, and track farms by region, district, and ownership
Diagnostics: AI-powered crop disease predictions using a TensorFlow h5 model
Taxonomy	manages crops, pests, and disease relationships
Analytics	Admin-only endpoints for biosecurity and platform summaries
Core	Shared utilities, including health checks and TensorFlow model loader
⚙️ Tech Stack
Backend Framework: Django 5.2 + Django REST Framework

AI/ML Integration: TensorFlow + NumPy + Pillow

Authentication: JWT (via SimpleJWT)

API Docs: drf-spectacular (Swagger & Redoc)

Database: SQLite (default), ready for PostgreSQL

CORS: Enabled for development

🚀 Getting Started
1️⃣ Clone the Repository
bash
git clone https://github.com/yennulomlarri/agri-sentio.git
cd agri-sentio-backend
2️⃣ Create and Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
If missing, generate one:

bash
pip freeze > requirements.txt
🧱 Environment Configuration
Create a .env file in the project root:

env
SECRET_KEY=django-insecure-agri-sentio-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
ACCESS_TOKEN_LIFETIME=3600
REFRESH_TOKEN_LIFETIME=86400
You can also add a public .env example for reference.

🧠 AI Model Integration
The TensorFlow integration is handled in core/ml_utils.py.

Place your trained model file at:

text
core/crop_disease_model.h5
If you don't have one yet, a mock-compatible structure allows simulated predictions until deployment.

📊 API Endpoints
Authentication Routes
Endpoint	Method	Description
/api/accounts/register/	POST	Register a new user
/api/accounts/login/	POST	Obtain JWT tokens
/api/accounts/profile/	GET	Get user profile data
Admin Analytics Endpoints
Endpoint	Method	Description
/api/admin/analytics/	GET	Analytics API overview
/api/admin/analytics/summary/	GET	Total users, farms, and diagnoses
/api/admin/analytics/biosecurity/	GET	Diagnosis counts by region and district
Authentication Required: Authorization: Bearer <your_access_token>

Core Utilities
/api/core/ - Core API utilities and system health

🧰 Development Commands
bash
# Run development server
python manage.py runserver

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
🔬 Testing
Use Postman or cURL for endpoint testing.

Example login:

bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
🧩 API Documentation
Open in browser:

Swagger UI: http://127.0.0.1:8000/api/docs/

Redoc: http://127.0.0.1:8000/api/redoc/

Schema: http://127.0.0.1:8000/api/schema/

🏗 Project Structure
text
agri-sentio-backend/
│
├── agrisentio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
├── farms/
├── diagnostics/
├── taxonomy/
├── analytics/
├── core/
│   ├── crop_disease_model.h5
│   └── ml_utils.py
│
├── manage.py
└── .env
🔮 Future Enhancements
Role-based access (Admin / Farmer)

Real TensorFlow model deployment

Interactive data visualization dashboards

React frontend integration

Docker & CI/CD setup

🧑‍💻 Author
Mateiyendou Kombat
📧 yennulomlarri@gmail.com
🎓 BSc. Statistics & Computer Science
🏫 KNUST | University of the People
💬 "Who is like God — Maker of Peace."

🏁 License
MIT License © 2025 Agri-Sentio Developers

