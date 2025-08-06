from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    # Endpoint for listing books and creating a new book
    path('books/', BookListCreate.as_view(), name='book-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific book by its primary key (pk)
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
]