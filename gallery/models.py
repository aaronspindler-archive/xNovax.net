from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=240)


class Photo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)