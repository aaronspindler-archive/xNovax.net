from django.shortcuts import render

from gallery.models import Event


def gallery(request):
    events = Event.objects.all()
    return render(request, 'gallery/list.html', {'events': events})
