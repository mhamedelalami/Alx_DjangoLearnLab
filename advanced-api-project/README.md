### API Endpoints

#### Books List and Filtering

**GET /api/books/**

This endpoint returns a list of all books. It supports the following query parameters for filtering, searching, and ordering:

- **Filtering:** Use `django-filter` to filter by fields.
  - `?title__icontains=the hobbit`
  - `?publication_year__gte=2000`
  - `?author__name__icontains=tolkien`

- **Searching:** Use the `search` parameter to perform a case-insensitive text search on `title` and `author__name`.
  - `?search=lord of the rings`

- **Ordering:** Use the `ordering` parameter to sort the results.
  - `?ordering=title` (ascending)
  - `?ordering=-publication_year` (descending)

  ## Testing

This project includes a comprehensive suite of unit tests to ensure the reliability and correctness of the API endpoints. The tests are written using Django's built-in unittest framework and Django REST Framework's APITestCase to simulate client requests.

- **How to Run Tests**

To execute the entire test suite, run the following command from your project's root directory:
Bash

python manage.py test api

This command will discover and run all tests within the api app. Django automatically sets up a separate, in-memory database for the tests, ensuring that your development data remains untouched.

- **What the Tests Cover**

The unit tests focus on the following key areas:

    - CRUD Operations: Verifying that the endpoints for creating, retrieving, updating, and deleting Book objects function correctly.

    - Permissions: Ensuring that IsAuthenticated and IsAuthenticatedOrReadOnly permissions are properly enforced. The tests check that authenticated users can perform privileged actions (e.g., creating a book) while unauthenticated users are correctly restricted.

    - Functionality: Validating that the API's filtering, searching, and ordering capabilities work as expected by making requests with various query parameters and asserting the returned data.

    - Status Codes: Confirming that each API request returns the appropriate HTTP status code (e.g., 200 OK, 201 Created, 403 Forbidden).

