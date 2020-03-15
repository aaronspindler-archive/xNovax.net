from django.shortcuts import render, get_object_or_404
from .models import Book


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/details.html', {'book':book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books':books})
