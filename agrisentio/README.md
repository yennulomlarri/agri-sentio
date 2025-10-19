# Agri-Sentio Backend API

## Project Overview

Agri-Sentio addresses critical agricultural challenges in Ghana through the use of mobile technology and artificial intelligence. This platform enables proactive crop health monitoring and supports national biosecurity decision-making. The backend constitutes a foundational capstone project that establishes a secure, scalable RESTful API for agricultural data management.

## Current Implementation Status

### ✅ Completed Foundation

The core project architecture is fully operational with these key achievements:

**Application Structure**
- Three modular Django applications: `accounts`, `farms`, and `diagnostics`
- Clear separation of concerns for maintainability and scalability
- Stable development environment with resolved dependency conflicts

**Database Architecture**
- Comprehensive model definitions completed
- Core Django migrations applied successfully
- SQLite database initialized and ready for custom schema implementation

**Administrative Setup**
- Superuser account created for system administration
- Django admin interface is fully accessible and functional
- Basic project configuration validated

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | Django 5.2.7 | Core application development |
| **API Framework** | Django REST Framework | RESTful API implementation |
| **Authentication** | JWT Tokens | Secure user access management |
| **Database** | SQLite (Development) | Data persistence layer |
| **Documentation** | OpenAPI/Swagger | API documentation generation |

## Project Setup

### Prerequisites
- Python 3.13+
- pip package manager
- Git version control

### Installation & Execution

1. **Clone and setup environment**
   ```bash
   git clone https://github.com/yennulomlarri/agri-sentio.git
   cd agri-sentio
   python -m venv venv
   source venv/Scripts/activate  # Windows Git Bash
   pip install -r requirements.txt
