from django.contrib import admin

from tools.models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short', 'target')


admin.site.register(ShortURL, ShortURLAdmin)
