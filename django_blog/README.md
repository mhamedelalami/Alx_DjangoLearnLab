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


