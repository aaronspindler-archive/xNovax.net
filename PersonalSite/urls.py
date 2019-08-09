from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import pages.views

urlpatterns = [
    path('', pages.views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
