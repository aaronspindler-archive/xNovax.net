from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import pages.views
import projects.views
import books.views
import courses.views
import tools.views

urlpatterns = [
    path('', pages.views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('project/<int:pk>/', projects.views.project_details, name='project_details'),
    path('book/<int:pk>/', books.views.book_details, name='book_detail'),
    path('course/<int:pk>/', courses.views.course_detail, name='course_detail'),
    path('tools/shorten', tools.views.url_shortener, name='url_shortener'),
    path('<str:pk>/', tools.views.url_shortened, name='url_shortened'),
    path('password', tools.views.password_generator, name='password_generator'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
