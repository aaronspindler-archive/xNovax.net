from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import pages.views
import books.views
import courses.views
import blog.views

urlpatterns = [
    path('', pages.views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('book/<int:pk>/', books.views.book_details, name='book_detail'),
    path('course/<int:pk>/', courses.views.course_detail, name='course_detail'),
    path('blog/<int:pk>/', blog.views.detail, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
