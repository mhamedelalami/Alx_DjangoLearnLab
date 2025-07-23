# LibraryProject Security and Permissions Documentation

## Security Measures Implemented

### 1. Secure Settings in `settings.py`
- `DEBUG = False` in production to prevent detailed error pages.
- Enabled browser security headers:
  - `SECURE_BROWSER_XSS_FILTER = True` to activate the XSS filter.
  - `X_FRAME_OPTIONS = 'DENY'` to prevent clickjacking.
  - `SECURE_CONTENT_TYPE_NOSNIFF = True` to prevent MIME sniffing.
- Cookie security:
  - `CSRF_COOKIE_SECURE = True` ensures CSRF cookies are sent only over HTTPS.
  - `SESSION_COOKIE_SECURE = True` ensures session cookies are sent only over HTTPS.
- Content Security Policy (CSP) headers added using `django-csp` middleware to control allowed sources for scripts, styles, images, fonts, etc.

### 2. CSRF Protection
- All HTML forms include `{% csrf_token %}` in templates to protect against Cross-Site Request Forgery.

### 3. Permissions and Access Control
- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) defined on the `Book` model.
- User groups (`Admins`, `Editors`, `Viewers`) created with specific permissions.
- Views are protected using `@permission_required` decorators to enforce access control.
- Only users with the appropriate permissions can create, edit, delete, or view books.

### 4. Safe Querying
- All database operations use Django ORM to avoid SQL injection.
- User inputs are validated via Django forms.

---

## How to Test

1. Assign users to different groups (Admins, Editors, Viewers) via Django admin.
2. Log in as different users and verify access restrictions are enforced correctly.
3. Inspect HTML forms to ensure CSRF tokens are present.
4. Check response headers to verify security headers (XSS filter, CSP, etc.) are set.

---

*This documentation serves as a quick overview of the security and permission practices implemented in this project.*
