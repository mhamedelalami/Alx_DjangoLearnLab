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