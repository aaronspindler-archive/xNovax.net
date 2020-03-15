from django.contrib.sitemaps import Sitemap

from .models import Course


class CourseSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Course.objects.all()
