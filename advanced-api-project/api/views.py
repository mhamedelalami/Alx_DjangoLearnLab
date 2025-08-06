from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books and creating new ones.
# It inherits from ListCreateAPIView, which combines list and create functionalities.
# IsAuthenticatedOrReadOnly ensures that unauthenticated users can only view, not create.
class BookListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing all books and creating a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view handles retrieving, updating, and deleting a single book.
# It inherits from RetrieveUpdateDestroyAPIView, which combines these three operations.
# IsAuthenticatedOrReadOnly ensures that unauthenticated users can only view a book,
# while authenticated users can update or delete it.
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, or deleting a specific book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]