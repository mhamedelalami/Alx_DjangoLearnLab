from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm  # Make sure you have this form created

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    """List all books, requires 'can_view' permission."""
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """Add a new book, requires 'can_create' permission."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """Edit an existing book, requires 'can_edit' permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """Delete a book, requires 'can_delete' permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
