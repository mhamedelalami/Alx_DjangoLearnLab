Perfect! Here’s a **complete `README.md`** combining your user authentication and posts/comments API documentation, ready to copy:

````markdown
# Social Media API

A simple Django REST Framework API for a social media platform. Users can register, log in, create posts, and engage with posts through comments.

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone <repository_url>
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
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Authentication

The API uses token-based authentication.

* **Register a user**: `/api/accounts/register/` (POST)
* **Login / Get token**: `/api/accounts/login/` (POST)

### **Register Request**

```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "yourpassword"
}
```

**Response**

```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
}
```

### **Login Request**

```json
{
    "username": "johndoe",
    "password": "yourpassword"
}
```

**Response**

```json
{
    "token": "your_auth_token"
}
```

> Include the token in the header for authenticated requests:

```
Authorization: Token <your_token_here>
```

---

## User Profile

**Endpoint:** `/api/accounts/profile/`
**Methods:** `GET`, `PUT`, `PATCH`

* **GET** → Retrieve your profile
* **PUT / PATCH** → Update your profile

**Example GET Response**

```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
}
```

---

## Posts API

**Endpoint:** `/api/posts/`
**Methods:** `GET`, `POST`

* **GET /api/posts/** → List all posts (paginated)
* **POST /api/posts/** → Create a new post

**POST Request**

```json
{
    "title": "My First Post",
    "content": "This is the content of my post."
}
```

**POST Response**

```json
{
    "id": 1,
    "author": "johndoe",
    "title": "My First Post",
    "content": "This is the content of my post.",
    "created_at": "2025-08-19T18:40:00Z",
    "updated_at": "2025-08-19T18:40:00Z"
}
```

**Endpoint:** `/api/posts/<id>/`
**Methods:** `GET`, `PUT`, `PATCH`, `DELETE`

* **GET** → Retrieve a single post
* **PUT / PATCH** → Update a post (author only)
* **DELETE** → Delete a post (author only)

**Filtering / Searching / Ordering**

```
GET /api/posts/?search=keyword&author__username=johndoe&ordering=-created_at
```

---

## Comments API

**Endpoint:** `/api/comments/`
**Methods:** `GET`, `POST`

* **GET /api/comments/** → List all comments (paginated)
* **POST /api/comments/** → Create a new comment

**POST Request**

```json
{
    "post": 1,
    "content": "This is a comment on the post."
}
```

**POST Response**

```json
{
    "id": 1,
    "post": 1,
    "author": "johndoe",
    "content": "This is a comment on the post.",
    "created_at": "2025-08-19T18:45:00Z",
    "updated_at": "2025-08-19T18:45:00Z"
}
```

**Endpoint:** `/api/comments/<id>/`
**Methods:** `GET`, `PUT`, `PATCH`, `DELETE`

* **GET** → Retrieve a single comment
* **PUT / PATCH** → Update a comment (author only)
* **DELETE** → Delete a comment (author only)

**Filtering / Searching / Ordering**

```
GET /api/comments/?search=keyword&post=1&author__username=johndoe&ordering=-created_at
```

---

## Permissions

* Users can only edit or delete their own posts and comments.
* Anyone can view posts and comments.

---

## Pagination

* List endpoints for posts and comments are paginated.
* Use `?page=<number>` to navigate pages.

---

## Notes

* All dates are in ISO 8601 format.
* Always include your authentication token when performing POST, PUT, PATCH, or DELETE requests.

```
