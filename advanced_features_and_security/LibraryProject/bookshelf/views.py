from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm  # Make sure this form validates inputs properly
from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    List all books.
    Access restricted to users with 'can_view' permission.
    Uses ORM query to avoid raw SQL injection risks.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """
    Add a new book.
    Access restricted to users with 'can_create' permission.
    Uses Django forms to validate and sanitize input data.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Ensures input is cleaned and valid before saving
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    Edit an existing book.
    Access restricted to users with 'can_edit' permission.
    Uses Django forms for validation and safe update.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():  # Validates input data before saving
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    Delete a book.
    Access restricted to users with 'can_delete' permission.
    The deletion only proceeds on POST request to prevent accidental deletes via GET.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
