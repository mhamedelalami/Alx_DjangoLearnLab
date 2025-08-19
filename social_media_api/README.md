# Social Media API

A Django REST Framework API that allows users to register, authenticate, create posts, comment on posts, follow other users, view a personalized feed, like posts, and receive notifications.

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

## 5. Likes & Notifications

### Like Model

Tracks which users have liked which posts.

```python
class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Notifications Model

Tracks interactions such as likes, new followers, and comments.

```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # e.g., "liked your post"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
```

---

### Like Endpoints

#### Like a Post

**POST** `/api/posts/<post_id>/like/`

* Authenticated users can like a post. Users cannot like the same post multiple times.

**Request Example:**

```http
POST /api/posts/12/like/
Authorization: Token <user_token>
```

**Response Example:**

```json
{
    "message": "You have liked the post."
}
```

#### Unlike a Post

**POST** `/api/posts/<post_id>/unlike/`

* Authenticated users can remove their like from a post.

**Request Example:**

```http
POST /api/posts/12/unlike/
Authorization: Token <user_token>
```

**Response Example:**

```json
{
    "message": "You have unliked the post."
}
```

---

### Notifications Endpoint

#### View Notifications

**GET** `/api/notifications/`

* Fetch all notifications for the authenticated user, ordered by timestamp (most recent first).
* Unread notifications are highlighted.

**Request Example:**

```http
GET /api/notifications/
Authorization: Token <user_token>
```

**Response Example:**

```json
[
    {
        "id": 1,
        "actor": "john_doe",
        "verb": "liked your post",
        "target": "Post: Amazing Sunset",
        "timestamp": "2025-08-19T15:23:00Z",
        "read": false
    },
    {
        "id": 2,
        "actor": "alice_smith",
        "verb": "started following you",
        "target": null,
        "timestamp": "2025-08-19T14:50:00Z",
        "read": true
    }
]
```

---

### Benefits

* **User Engagement:** Encourages interaction with posts and other users.
* **Real-time Feedback:** Users know when their content is liked or when they have new followers.
* **Retention:** Notifications help users stay active on the platform.

---

## 6. Permissions & Notes

* Only authenticated users can create posts/comments, follow/unfollow, like/unlike posts, view notifications, or see their feed.
* Users can only edit or delete their own posts/comments.
* Pagination and filtering are available for posts and comments.

---

Here’s a final continuation for your README that completes it with **Step 7: Documentation and Final Testing**, deployment notes, and final remarks:

## 7. Deployment & Production

### Environment Configuration

For production, the following environment variables should be set (e.g., in Railway, Heroku, or another hosting service):

```env
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=your-production-domain.com
DATABASE_URL=postgres://DB_USER:DB_PASSWORD@DB_HOST:DB_PORT/DB_NAME
SECURE_SSL_REDIRECT=True
````

### Production Settings in `settings.py`

* `DEBUG = False`

* `ALLOWED_HOSTS` configured for your domain or hosting service

* Security settings enabled:

  * `SECURE_BROWSER_XSS_FILTER = True`
  * `X_FRAME_OPTIONS = 'DENY'`
  * `SECURE_CONTENT_TYPE_NOSNIFF = True`
  * `CSRF_COOKIE_SECURE = True`
  * `SESSION_COOKIE_SECURE = True`

* Static files served via WhiteNoise:

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

* Database configured via `dj-database-url` to handle PostgreSQL URLs.

### Deployment Steps (Example with Railway)

1. Connect your GitHub repository to Railway.
2. Set the environment variables listed above in Railway.
3. Railway will automatically build and deploy your Django API.
4. Ensure migrations are applied via Railway’s CLI or dashboard:

```bash
railway run python manage.py migrate
```

5. Collect static files:

```bash
railway run python manage.py collectstatic --noinput
```

### Final Testing

* Verify all endpoints work as expected:

  * User registration & login
  * Post creation, update, deletion
  * Comment creation, update, deletion
  * Like/unlike functionality
  * Follows & feed endpoints
  * Notifications endpoint
* Ensure only authenticated users can perform protected actions.
* Check pagination, filtering, and ordering work correctly in production.
* Verify HTTPS and security settings are properly applied.

---

## 8. Additional Notes

* The API is ready for real-world usage and can be integrated with frontend clients.
* Use token-based authentication for API requests.
* Keep the `.env` file secret; never commit it to public repositories.
* Regularly monitor logs and perform maintenance for dependencies and security updates.

---

## Live Application URL

`<insert-your-live-url-here>`

---

## License

MIT License
