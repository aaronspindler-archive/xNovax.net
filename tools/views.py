from django.shortcuts import render
from .forms import ShortenURLForm


def url_shortener(request):
	form = ShortenURLForm()
	if request.method == 'POST':
		pass

	return render(request, 'tools/url_shortener.html', {'form': form})


def url_shortened(request, pk):
	return render(request, 'tools/url_shortener.html')


def password_generator(request):
	return render(request, 'tools/password_generator.html')