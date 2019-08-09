from django.shortcuts import render
from books.models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'pages/home.html', {'books':books})
