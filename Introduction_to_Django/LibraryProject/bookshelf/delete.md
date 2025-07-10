In [4]: book.delete()
   ...: print(Book.objects.all())  # Should show an empty queryset     
   ...:
<QuerySet []>