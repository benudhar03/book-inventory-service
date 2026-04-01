# 📚 Async Book Inventory Service API using FastAPI and MongoDB

A scalable backend application built using **FastAPI** and **MongoDB**, supporting full CRUD operations, advanced search, validation, and async testing.

---

## 🚀 Features

* ✅ Create, Read, Update, Delete (CRUD) APIs
* 🔍 Search books by title (with fallback suggestions)
* 📦 Filter books by publisher
* 📊 Show only in-stock books
* 🔄 Toggle stock status (true ↔ false)
* ✅ Input validation using Pydantic
* ⚡ Async API handling
* 🧪 Unit testing using pytest + httpx
* 🐳 Dockerized application
* ☸️ Kubernetes deployment ready

---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Database**: MongoDB
* **Async Driver**: Motor
* **Validation**: Pydantic
* **Testing**: pytest, pytest-asyncio, httpx
* **Containerization**: Docker
* **Orchestration**: Kubernetes

---

## 📁 Project Structure

```
fastapi-mongo-crud/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── book_routes.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── book_model.py
│   ├── schemas/
│   │   └── book_schema.py
│   ├── services/
│   │   └── book_service.py
│   └── main.py
│
├── tests/
│   └── test_books_api.py
│
├── k8s/
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd fastapi-mongo-crud
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=books_py_db
```

---

### 5️⃣ Run Application

```
uvicorn app.main:app --reload
```

👉 API Docs:
http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

### 🔹 Create Book

```
POST /books/
```

### 🔹 Get All Books (Only In-Stock)

```
GET /books/
```

### 🔹 Search Books by Title

```
GET /books/search?title=Clean
```

### 🔹 Get Books by Publisher

```
GET /books/publisher/{publisher}
```

### 🔹 Toggle Stock

```
PATCH /books/{book_id}/toggle-stock
```

#### ✅ Sample Response:

```json
{
  "message": "Book stock status toggled successfully",
  "book": {
    "id": "123",
    "title": "Clean Code",
    "in_stock": false
  }
}
```

---

## 🧪 Running Tests

### Install test dependencies

```
pip install pytest pytest-asyncio httpx pytest-mock
```

### Run tests

```
pytest -v
```

---

## 🧠 Testing Approach

* Async API testing using `httpx.AsyncClient`
* `ASGITransport` used for FastAPI compatibility
* Service layer mocked using `pytest-mock`
* No real DB calls during unit tests

---

## 🐳 Docker Setup

### Build Image

```
docker build -t fastapi-crud-app .
```

### Run Container

```
docker run -p 8000:8000 fastapi-crud-app
```

---

## ☸️ Kubernetes Deployment

Apply configs:

```
kubectl apply -f k8s/
```

---

## 📊 Future Enhancements

* 🔐 Authentication & Authorization (JWT)
* 📈 Logging & Monitoring
* 📊 Test Coverage Reports
* 🔁 CI/CD Pipeline (GitHub Actions)
* 📦 Helm Charts for deployment

---

## 🧠 Key Learnings

* Async API design using FastAPI
* MongoDB integration with Motor
* Clean architecture (controller → service → DB)
* API validation with Pydantic
* Writing async test cases
* Mocking dependencies in unit tests
* Docker & Kubernetes basics

---

## 👨‍💻 Author

**Benudhar Behera**
Senior Backend Engineer | Java | Python | Distributed Systems

---

## ⭐ Contribution

Feel free to fork, improve, and raise PRs 🚀
