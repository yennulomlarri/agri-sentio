🌾 Agri-Sentio Backend API
Crop Disease Detection & Farm Analytics Platform

📘 Overview
Agri-Sentio is a modern AI-powered crop disease detection and farm management platform designed to support Ghana's agricultural sector. This repository contains the complete Django REST Framework backend, which provides robust APIs for user authentication, farm management, crop diagnostics, taxonomy management, administrative analytics, and TensorFlow-based disease prediction.

🧩 Features
Module	Description
Accounts	Custom user model with JWT authentication implementation
Farms: Farm registration and management with regional tracking capabilities
Diagnostics	AI-powered crop disease predictions using TensorFlow models
Taxonomy: Comprehensive crop, pest, and disease relationship management
Analytics	Admin-only endpoints for biosecurity monitoring and platform statistics
Core	Shared utilities, including system health checks and AI model integration
⚙️ Technology Stack
Backend Framework: Django 5.2 with Django REST Framework

AI/ML Integration: TensorFlow, NumPy, and Pillow for image processing

Authentication: JSON Web Tokens (JWT) via SimpleJWT

API Documentation: drf-spectacular with Swagger and Redoc interfaces

Database: SQLite (development), configurable for PostgreSQL via environment variables

CORS: Enabled for all origins during local development

🚀 Getting Started
1️⃣ Clone the Repository
bash
git clone https://github.com/yennulomlarri/agri-sentio.git
cd agri-sentio-backend
2️⃣ Create and Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
If you need to generate a requirements file:

bash
pip freeze > requirements.txt
🧱 Environment Configuration
Create a .env file in the project root with the following variables:

env
SECRET_KEY=django-insecure-agri-sentio-backend-2025
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
🧠 AI Model Integration
The platform integrates TensorFlow for intelligent disease prediction through core/ml_utils.py. Place your trained model file at:

text
core/crop_disease_model.h5
The system includes a mock model loader for development and testing purposes.

📊 API Endpoints
Authentication Routes
Endpoint	Method	Description
/api/accounts/register/	POST	Register new user accounts
/api/accounts/login/	POST	Obtain JWT authentication tokens
/api/accounts/profile/	GET	Retrieve authenticated user information
Admin Analytics Endpoints
Endpoint	Method	Description
/api/admin/analytics/	GET	Analytics API overview and available endpoints
/api/admin/analytics/summary/	GET	System statistics (users, farms, diagnoses)
/api/admin/analytics/biosecurity/	GET	Regional disease outbreak aggregation
Authentication Required: Authorization: Bearer <your_access_token>

Core Utilities
/api/core/ - Core API utilities and health checks

🧰 Development Commands
bash
# Start development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Administrative access
python manage.py createsuperuser

# Development tools
python manage.py shell
🔬 Testing
Test API endpoints using curl or Postman:

bash
# Test analytics endpoint
curl http://127.0.0.1:8000/api/admin/analytics/

# Test authentication
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
🧩 API Documentation
Access comprehensive API documentation through:

Swagger UI: http://127.0.0.1:8000/api/docs/

Redoc: http://127.0.0.1:8000/api/redoc/

API Schema: http://127.0.0.1:8000/api/schema/

🏗 Project Architecture
text
agri-sentio-backend/
├── agrisentio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
├── farms/
├── diagnostics/
├── taxonomy/
├── analytics/
├── core/
│   ├── crop_disease_model.h5
│   └── ml_utils.py
├── manage.py
└── .env
Each module maintains independent URL routing, views, and models for optimal modular organization.

🔮 Future Enhancements
Advanced role-based permission systems

Production-ready TensorFlow model deployment

Comprehensive data visualization dashboard

Frontend integration with modern frameworks

Docker containerization and CI/CD pipeline implementation

🧑‍💻 Author
Mateiyendou Mantot Kombat
📧 yennulomlarri@gmail.com
🎓 BSc. Statistics & Computer Science
🏫 KNUST | University of the People

🏁 License
MIT License © 2025 Agri-Sentio Developers

