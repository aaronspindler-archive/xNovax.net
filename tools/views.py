from django.shortcuts import render


def url_shortener(request):
	return render(request, 'tools/url_shortener.html')


def url_shortened(request, pk):
	return render(request, 'tools/url_shortener.html')


def password_generator(request):
	return render(request, 'tools/password_generator.html')