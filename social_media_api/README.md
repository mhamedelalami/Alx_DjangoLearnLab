# Social Media API

A simple **Django REST Framework API** for user authentication and profile management.  
Users can register, log in, and manage their profiles using token-based authentication.

---

## Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd social_media_api
````

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install django djangorestframework
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## User Authentication

### Register a New User

* **Endpoint:** `POST /api/accounts/register/`
* **Request Body (JSON):**

```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "TestPass123",
  "bio": "Hello, I am a test user."
}
```

* **Response:** Returns user details (excluding password).

---

### Login

* **Endpoint:** `POST /api/accounts/login/`
* **Request Body (JSON):**

```json
{
  "username": "testuser",
  "password": "TestPass123"
}
```

* **Response:** Returns a JSON object with:

```json
{
  "token": "xxxxxxxxxxxxxxxxxxxx",
  "user_id": 1,
  "username": "testuser"
}
```

* **Usage:** Include the token in the `Authorization` header for protected endpoints:

```
Authorization: Token <your_token_here>
```

---

## User Model Overview

The custom user model extends Django’s `AbstractUser` and includes:

* **username** – required
* **email** – optional
* **bio** – short biography of the user
* **profile\_picture** – image for user avatar
* **followers** – ManyToMany field referencing other users (symmetrical=False)

---

