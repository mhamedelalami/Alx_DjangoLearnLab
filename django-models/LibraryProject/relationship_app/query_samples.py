from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author_name = "George Orwell"
    author = Author.objects.filter(name=author_name).first()
    if author:
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No author found with name {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    library = Library.objects.filter(name=library_name).first()
    if library:
        print(f"Books in library {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    else:
        print(f"No library found with name {library_name}")

    # 3. Retrieve the librarian for a library
    if library:
        librarian = Librarian.objects.filter(library=library).first()
        if librarian:
            print(f"Librarian for library {library_name}: {librarian.name}")
        else:
            print(f"No librarian assigned to library {library_name}")
    if __name__ == "__main__":
        run_queries()   

        