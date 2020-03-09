from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
import pages.views
import projects.views
import books.views
import courses.views
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
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                  path('admin/', admin.site.urls, name='admin'),
                  path('project/<int:pk>/', projects.views.project_details, name='project_details'),
                  path('book/<int:pk>/', books.views.book_details, name='book_detail'),
                  path('course/<int:pk>/', courses.views.course_detail, name='course_detail'),
                  path('tools/shorten', tools.views.url_shortener, name='url_shortener'),
                  path('<str:pk>/', tools.views.url_shortened, name='url_shortened'),
                  path('password', tools.views.password_generator, name='password_generator'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
