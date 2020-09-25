from django.contrib import admin

from .models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'description', 'github_link', 'deployment_link')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
