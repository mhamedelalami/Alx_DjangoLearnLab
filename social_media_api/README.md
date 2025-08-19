Here’s a complete, ready-to-copy README combining **setup, user registration/authentication, posts/comments, and follows/feed**:

---

# Social Media API

A Django REST Framework API that allows users to register, authenticate, create posts, comment on posts, follow other users, and view a personalized feed.

---

## 1. Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd social_media_api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

---

## 2. User Registration & Authentication

### Register

**POST** `/api/accounts/register/`

**Request:**

```json
{
    "username": "user123",
    "email": "user@example.com",
    "password": "securepassword"
}
```

**Response:**

```json
{
    "id": 1,
    "username": "user123",
    "email": "user@example.com"
}
```

### Login / Get Token

**POST** `/api/accounts/login/`

**Request:**

```json
{
    "username": "user123",
    "password": "securepassword"
}
```

**Response:**

```json
{
    "token": "abcd1234efgh5678",
    "user_id": 1,
    "username": "user123"
}
```

### User Profile

**GET / PUT** `/api/accounts/profile/`

* Retrieve or update the logged-in user’s profile.

---

## 3. Posts & Comments

### Post Model

* `author`: User
* `title`: string
* `content`: string
* `created_at`: datetime
* `updated_at`: datetime

### Comment Model

* `post`: Post
* `author`: User
* `content`: string
* `created_at`: datetime
* `updated_at`: datetime

### Endpoints

#### Posts

* **GET** `/api/posts/` – List all posts (supports filtering by author, search by title/content, ordering)
* **POST** `/api/posts/` – Create a new post
* **GET / PUT / DELETE** `/api/posts/<id>/` – Retrieve, update, or delete a post (only author can modify)

#### Comments

* **GET** `/api/comments/` – List all comments (filter by author or post)
* **POST** `/api/comments/` – Create a new comment
* **GET / PUT / DELETE** `/api/comments/<id>/` – Retrieve, update, or delete a comment (only author can modify)

**Example Post Response:**

```json
{
    "id": 1,
    "author": "user123",
    "title": "My First Post",
    "content": "This is the content of my post.",
    "created_at": "2025-08-19T15:30:00Z",
    "updated_at": "2025-08-19T15:30:00Z"
}
```

**Example Comment Response:**

```json
{
    "id": 1,
    "post": 1,
    "author": "friend456",
    "content": "Great post!",
    "created_at": "2025-08-19T16:00:00Z",
    "updated_at": "2025-08-19T16:00:00Z"
}
```

---

## 4. User Follows & Feed

### User Model Update

```python
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following', blank=True
    )
```

* `followers`: users who follow this user
* `following`: users this user follows (reverse relation)

### Follow Endpoints

#### Follow a user

**POST** `/api/accounts/follow/<user_id>/`

**Response Example:**

```json
{
    "message": "You are now following user123."
}
```

#### Unfollow a user

**POST** `/api/accounts/unfollow/<user_id>/`

**Response Example:**

```json
{
    "message": "You have unfollowed user123."
}
```

### Feed Endpoint

**GET** `/api/posts/feed/`

* Returns posts from users the current user follows, ordered by most recent first.

**Response Example:**

```json
[
    {
        "id": 1,
        "author": "user123",
        "title": "My First Post",
        "content": "This is the content of my post.",
        "created_at": "2025-08-19T15:30:00Z",
        "updated_at": "2025-08-19T15:30:00Z"
    }
]
```

---

## 5. Permissions & Notes

* Only authenticated users can create posts/comments, follow/unfollow, or view their feed.
* Users can only edit or delete their own posts/comments.
* Pagination and filtering are available for posts and comments.

---

