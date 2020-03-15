from django.shortcuts import render, redirect

from utils import random_string
from .forms import ShortenURLForm
from .models import ShortURL


def url_shortener(request):
    form = ShortenURLForm()
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            shortenedurl = ShortURL()
            short = random_string.generate_short()

            while True:
                # TODO: Check if the target URL already exists and if it does, don't create another entry, just point to the old one
                # Check if the short string already exists
                check = ShortURL.objects.filter(short=short)
                # If not save to DB
                if check.count() == 0:
                    shortenedurl.short = short
                    shortenedurl.target = form.cleaned_data['url']
                    shortenedurl.save()
                    return render(request, 'tools/url_shortened.html', {'shortenedurl': shortenedurl})

                # If it does, generate another with length + 1
                short = random_string.generate_short(len(short) + 1)

    return render(request, 'tools/url_shortener.html', {'form': form})


def url_shortened(request, pk):
    try:
        short_url = ShortURL.objects.get(pk=pk)
        return redirect(short_url.target)
    except Exception:
        pass


def password_generator(request):
    if request.method == 'POST':
        pass
    return render(request, 'tools/password_generator.html')
