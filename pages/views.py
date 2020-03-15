from django.shortcuts import render
from projects.models import Project
from books.models import Book
from courses.models import Course
from utils import medium


def home(request):
	posts = medium.get_posts('aaron_spindler', 3)
	projects = Project.objects.all()[:3]
	books = Book.objects.all()[:3]
	courses = Course.objects.all()[:3]
	return render(request, 'pages/home.html', {'projects': projects, 'books': books, 'courses': courses, 'posts': posts})
