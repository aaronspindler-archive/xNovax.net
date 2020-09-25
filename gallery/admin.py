from django.contrib import admin

from .models import Event, Photo


class EventAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'event', 'image')


admin.site.register(Event, EventAdmin)
admin.site.register(Photo, PhotoAdmin)
