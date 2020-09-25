from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instituition', 'course_code', 'external_link', 'certificate_link')


admin.site.register(Course, CourseAdmin)
