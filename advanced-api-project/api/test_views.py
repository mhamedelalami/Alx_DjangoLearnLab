from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an author and some books to test against
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book1 = Book.objects.create(title='The Hobbit', publication_year=1937, author=self.author)
        self.book2 = Book.objects.create(title='The Lord of the Rings', publication_year=1954, author=self.author)

        # URLs for our endpoints
        self.list_create_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_book_list(self):
        """
        Test that an unauthenticated user can view the list of books.
        """
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_create_authenticated(self):
        """
        Test that an authenticated user can create a new book.
        """
        self.client.login(username='testuser', password='testpassword') # Use self.client.login()
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Book')

    def test_book_create_unauthenticated(self):
        """
        Test that an unauthenticated user cannot create a new book.
        """
        data = {'title': 'Forbidden Book', 'publication_year': 2024, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update(self):
        """
        Test that an authenticated user can update an existing book.
        """
        self.client.login(username='testuser', password='testpassword') # Use self.client.login()
        updated_data = {'title': 'The Hobbit (Updated)', 'publication_year': 1937, 'author': self.author.pk}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Hobbit (Updated)')

    def test_book_delete(self):
        """
        Test that an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword') # Use self.client.login()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_list_filter_search_ordering(self):
        """
        Test filtering, searching, and ordering functionalities.
        """
        # Test filtering by publication year
        response = self.client.get(self.list_create_url, {'publication_year': 1937})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Test searching by author name
        response = self.client.get(self.list_create_url, {'search': 'Tolkien'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Test ordering by publication year in descending order
        response = self.client.get(self.list_create_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')