from django.shortcuts import render, get_object_or_404
from .models import Book

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/details.html', {'book':book})
