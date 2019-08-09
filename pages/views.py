from django.shortcuts import render
from books.models import Book
from blog.models import Blog
from courses.models import Course

def home(request):
    books = Book.objects.all()
    courses = Course.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'pages/home.html', {'books':books,'courses': courses, 'blogs':blogs})
