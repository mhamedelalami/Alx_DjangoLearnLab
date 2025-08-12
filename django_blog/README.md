Here’s your authentication documentation properly formatted as a `README.md` file:

```markdown
# Authentication System Documentation

## Overview

This Django project implements a simple user authentication system that allows users to:

- Register for an account
- Log in to their account
- Log out of the system
- View & update their profile (email address)

The authentication uses Django's built-in authentication framework with a custom registration form and profile management view.

---

## How the Authentication Works

### 1. User Registration

**File:** `blog/views.py` → `register()` function  

**Process:**
1. A user visits `/register/` to sign up.
2. `CustomUserCreationForm` validates the input.
3. If valid, a new `User` object is created in the database.
4. The user is automatically logged in using `login(request, user)`.
5. The user is redirected to their profile page.

**Template:** `blog/templates/blog/register.html`  
**Form:** `blog/forms.py` → `CustomUserCreationForm`

---

### 2. User Login

**Files:** `django_blog/urls.py` and `settings.py` configuration  

**Process:**
1. User visits `/login/`.
2. Django validates username & password.
3. If valid, user is redirected to the next page or homepage.

**Template:** `registration/login.html`

---

### 3. User Logout

**File:** `django_blog/urls.py`  

**Process:**
1. User clicks Logout.
2. Session is cleared.
3. User is redirected to homepage or a confirmation page.

---

### 4. Profile Management

**File:** `blog/views.py` → `profile()` function  

**Process:**
1. Profile page requires login (`@login_required`).
2. User can update their email address.
3. Changes are saved to the `User` model.

**Template:** `blog/templates/blog/profile.html`

---

## Authentication Flow Diagram

```

\[Register] ---> \[Login] ---> \[Profile Page] ---> \[Update Profile]
\-----------------------> \[Logout] <------------------/

```

---

## How to Test Each Authentication Feature

### 1. Test Registration
- Go to: `http://127.0.0.1:8000/register/`
- Fill in username, email, and matching passwords.
- Submit and check:
  - User is created in the database.
  - User is automatically logged in and redirected to `/profile/`.

### 2. Test Login
- Go to: `http://127.0.0.1:8000/login/`
- Enter valid credentials of an existing user.
- Submit and check:
  - User is redirected to profile/home.
  - Incorrect credentials should show an error message.

### 3. Test Logout
- While logged in, go to: `http://127.0.0.1:8000/logout/`
- Check that:
  - User is redirected (or shown a logout confirmation page).
  - Trying to access `/profile/` redirects to `/login/`.

### 4. Test Profile Update
- Log in and go to: `http://127.0.0.1:8000/profile/`
- Enter a new email and submit.
- Check that:
  - Success message appears.
  - Email is updated in the database.

---

## Security Notes
- The profile page is protected by `@login_required`.
- Django's password hashing ensures passwords are never stored in plain text.
- CSRF tokens are used in all POST requests for form security.
```

# Blog Post Management Features Documentation

## Overview

This Django blog project includes full CRUD (Create, Read, Update, Delete) functionality for blog posts. Authenticated users can create, edit, and delete their own posts. All users, whether authenticated or not, can view the list of posts and individual post details.

## Features

### 1. List Posts

- **View:** `PostListView`  
- **URL:** `/posts/`  
- **Description:** Displays all blog posts ordered by published date (newest first). Accessible to all users.

### 2. View Post Details

- **View:** `PostDetailView`  
- **URL:** `/posts/<post_id>/`  
- **Description:** Shows the full content of a specific post. Accessible to all users.

### 3. Create a New Post

- **View:** `PostCreateView`  
- **URL:** `/posts/new/`  
- **Access:** Only logged-in users  
- **Description:** Authenticated users can create new posts. The author is automatically set to the logged-in user. On successful creation, users are redirected to the post detail page.

### 4. Update an Existing Post

- **View:** `PostUpdateView`  
- **URL:** `/posts/<post_id>/edit/`  
- **Access:** Only the post’s author  
- **Description:** Post authors can edit their own posts. Unauthorized users cannot access this view.

### 5. Delete a Post

- **View:** `PostDeleteView`  
- **URL:** `/posts/<post_id>/delete/`  
- **Access:** Only the post’s author  
- **Description:** Post authors can delete their posts. Upon deletion, users are redirected to the list of posts.

## Permissions and Security

- The creation, update, and delete views are protected by `LoginRequiredMixin` and `UserPassesTestMixin` to ensure only authenticated authors can modify their posts.
- The list and detail views are publicly accessible.
- Proper URL access restrictions prevent unauthorized editing or deleting.
- CSRF protection is enabled for all forms.
  
## Usage Instructions

- **To create a post:** Log in, then visit `/posts/new/` and fill out the form.
- **To edit or delete a post:** Visit the post detail page, then use the provided links/buttons (ensure you are the author).
- **To view posts:** Visit `/posts/` for a list or `/posts/<post_id>/` for details.

## Notes

- The `Post` model defines a `get_absolute_url()` method which is used to redirect users to the post detail page after creating or updating posts.
- All templates follow consistent styling to integrate smoothly with the site's CSS.
- Testing includes verifying form submissions, permission checks, and navigation flows.

# Comment System

## Overview

This project includes a comment system to enhance interactivity by allowing users to read and engage with blog posts through comments. Authenticated users can post, edit, and delete their comments, fostering community discussions.

## Features

- **View Comments:** All visitors can see comments under each blog post.
- **Add Comments:** Only logged-in users can add new comments.
- **Edit Comments:** Users can edit only their own comments.
- **Delete Comments:** Users can delete only their own comments.
- Comments are shown in reverse chronological order (newest first).

## Models

- **Comment**
  - `post`: ForeignKey linking to the associated blog post.
  - `author`: ForeignKey to the user who wrote the comment.
  - `content`: TextField containing the comment text.
  - `created_at`: DateTimeField marking the comment creation time.
  - `updated_at`: DateTimeField marking the last update time.

## Views & Permissions

- **Add Comment:** Function-based view `add_comment` requiring authentication.
- **Edit Comment:** Class-based view `CommentUpdateView`, restricted to comment authors.
- **Delete Comment:** Class-based view `CommentDeleteView`, restricted to comment authors.
- **Post Detail:** Displays the post content, all related comments, and a form to add a new comment (for authenticated users).

## URLs

- Create comment: `/posts/<post_pk>/comments/new/`
- Edit comment: `/comments/<comment_pk>/edit/`
- Delete comment: `/comments/<comment_pk>/delete/`

## Templates

- Comments appear on the blog post detail page.
- Separate templates handle comment creation/editing (`comment_form.html`) and deletion confirmation (`comment_confirm_delete.html`).

## Usage Instructions

1. Navigate to a blog post detail page.
2. Scroll to the comments section to view existing comments.
3. If logged in, submit a new comment using the provided form.
4. Edit or delete your own comments using the links displayed next to your comments.
5. If not logged in, users are prompted to log in to add comments.

---
