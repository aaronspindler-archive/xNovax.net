from django.shortcuts import render

from utils import random_string
from .forms import ShortenURLForm
from .models import ShortURL


def url_shortener(request):
	form = ShortenURLForm()
	if request.method == 'POST':
		form = ShortenURLForm(request.POST)
		if form.is_valid():
			shortenedurl = ShortURL()

			# Generate a short string
			short = random_string.generate_short()

			# Check if the short string already exists
			check = ShortURL.objects.filter(short=short)
			# If not save to DB
			if check.count() == 0:
				shortenedurl.short = short
				shortenedurl.target = form.cleaned_data['url']
				shortenedurl.save()

			# If it does, generate another with length + 1
			short = random_string.generate_short(len(short) + 1)


	return render(request, 'tools/url_shortener.html', {'form': form})


def url_shortened(request, pk):
	return render(request, 'tools/url_shortener.html')


def password_generator(request):
	return render(request, 'tools/password_generator.html')