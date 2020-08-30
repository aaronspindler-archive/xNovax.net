from django.shortcuts import render

from books.models import Book
from courses.models import Course
from projects.models import Project, Technology
from utils import medium

from datetime import datetime


def home(request):
	posts = medium.get_posts('aaron_spindler', 3)

	for post in posts:
		pubDate = datetime.strptime(post['pubDate'], '%Y-%m-%d %H:%M:%S')
		post['pubDate'] = pubDate

	projects = Project.objects.all()[:3]
	books = Book.objects.all()[:3]
	courses = Course.objects.all()[:3]
	technologies = Technology.objects.all()
	return render(request, 'pages/home.html', {'projects': projects, 'books': books, 'courses': courses, 'posts': posts, 'technologies': technologies})


def computer_gear(request):
	return render(request, 'pages/computer_gear.html')
