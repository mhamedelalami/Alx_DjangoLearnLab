from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# The BookSerializer handles the serialization and deserialization of Book objects.
# It includes custom validation to ensure the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    def validate_publication_year(self, value):
        """
        Custom validator to ensure the publication year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer serializes Author objects. It includes a nested BookSerializer
# to display all books associated with an author, demonstrating a one-to-many relationship.
class AuthorSerializer(serializers.ModelSerializer):
    # This field uses the BookSerializer to serialize related books. The 'many=True'
    # argument indicates that the author can have multiple books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']