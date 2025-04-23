
# 🛒 Ecommerce API

A Django REST Framework-based backend system for managing **Products**, **Customers**, and **Orders** with features including:

- JWT authentication
- MySQL database support
- Scheduled background syncing with Celery + Redis
- Duplicate/merge logic for external product/customer data
- Swagger/OpenAPI documentation
- Unit & integration tests with pytest and coverage report

---

## 🧱 Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT (SimpleJWT)
- **Database**: MySQL
- **Worker**: Celery + Redis
- **Docs**: drf-yasg (Swagger/OpenAPI)
- **Tests**: Pytest, Pytest-django, Pytest-cov

---

## ⚙️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DB_NAME=ecommerce_db
DB_USER=root
DB_PASSWORD=yourpassword
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Start development server

```bash
python manage.py runserver
```

### 8. Start Redis and Celery worker (in separate terminals)

**Redis**:
```bash
redis-server
```

**Celery**:
```bash
celery -A ecommerce_api worker --loglevel=info
```

---

## 🔐 Authentication

Obtain token:
```bash
POST /api/token/
{
  "username": "dell456",
  "password": "kanhapanda123"
}
```

Use the `access` token in your headers:

```
Authorization: Bearer <your_token>
```

---

## 🚀 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/products/` | List all products |
| `POST /api/products/` | Create a product |
| `GET /api/products/{id}/` | Retrieve a product |
| `PUT /api/products/{id}/` | Update a product |
| `DELETE /api/products/{id}/` | Delete a product |
| `GET /api/customers/` | List all customers |
| `POST /api/customers/` | Create a customer |
| `POST /api/refresh/` | Trigger background sync |
| `GET /swagger/` | Swagger/OpenAPI Docs |

---

## 🔄 Sync & Deduplication Logic

- The `/api/refresh/` endpoint triggers `sync_data` via Celery.
- External dummy product/customer data is fetched and:
  - Updated if `sku` or `email` matches existing entries.
  - Created if not found.
- Partial failures and exceptions are logged.

---

## 📊 Swagger Documentation

View at:  
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

> To publish, export JSON from Swagger UI and upload to [SwaggerHub](https://swagger.io/tools/swaggerhub/).

---

## ✅ Running Tests

```bash
pytest --cov=api --cov-report=term-missing
```

Covers:
- CRUD operations
- Sync tasks
- Auth & protected routes
- Deduplication logic

---

## 🗂️ Folder Structure

```
ecommerce_api/
├── api/                # App for products, customers, orders
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── urls.py
│   └── tests/
├── ecommerce_api/      # Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## 📌 Design Decisions & Features

- **JWT** for secure token-based authentication.
- **Celery + Redis** for async background tasks (data sync).
- **`update_or_create`** for deduplication logic.
- **Swagger Docs** for developer-friendly API usage.
- **Tests** written with Pytest, coverage >70%.
- **No Docker or webhook used**, following project instructions.

---

## 👨‍💻 Author

Built with 💻 by [Srikanta panda]

---

## 📅 Due Date

Final Submission: **April 23th, evening**
