In [1]: from bookshelf.models import Book
   ...:
   ...: book = Book.objects.create(title="1984", author="George Orwell 
      ⋮ ", publication_year=1949)
   ...: print(book)
   ...:
1984 by George Orwell (1949)



In [2]: book = Book.objects.get(title="1984")
   ...: print(book.title, book.author, book.publication_year)
   ...:
1984 George Orwell 1949



In [3]: book.title = "Nineteen Eighty-Four"
   ...: book.save()
   ...: print(book.title)
   ...:
Nineteen Eighty-Four



In [4]: book.delete()
   ...: print(Book.objects.all())  # Should show an empty queryset     
   ...:
<QuerySet []>