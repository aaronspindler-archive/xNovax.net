from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

import books.views
import courses.views
import gallery.views
import pages.views
import projects.views
import tools.views

from books.sitemaps import BookSitemap
from courses.sitemaps import CourseSitemap
from pages.sitemaps import PageSitemap
from projects.sitemaps import ProjectSitemap

sitemaps = {
    'pages': PageSitemap,
    'project': ProjectSitemap,
    'course': CourseSitemap,
    'book': BookSitemap,
}

urlpatterns = [
                path('', pages.views.home, name='home'),
                path('gear/computer', pages.views.computer_gear, name='computer_gear'),
                path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                path('admin/', admin.site.urls, name='admin'),
                path('gallery', gallery.views.gallery, name='gallery'),
                path('projects', projects.views.project_list, name='project_list'),
                path('project/<int:pk>/', projects.views.project_details, name='project_details'),
                path('books', books.views.book_list, name='book_list'),
                path('book/<int:pk>/', books.views.book_details, name='book_detail'),
                path('courses', courses.views.course_list, name='course_list'),
                path('course/<int:pk>/', courses.views.course_detail, name='course_detail'),
                path('tools/shorten', tools.views.url_shortener, name='url_shortener'),
                path('passgenerator', tools.views.password_generator, name='password_generator'),
                path('<str:pk>/', tools.views.url_shortened, name='url_shortened'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
