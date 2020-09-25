from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'favourite_passage', 'cover')


admin.site.register(Book, BookAdmin)
