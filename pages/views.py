from django.shortcuts import render
from projects.models import Project
from books.models import Book
from blog.models import Blog
from courses.models import Course

def home(request):
    projects = Project.objects.all()
    books = Book.objects.all()
    courses = Course.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'pages/home.html', {'projects':projects,'books':books,'courses': courses, 'blogs':blogs})
