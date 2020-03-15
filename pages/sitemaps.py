from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PageSitemap(Sitemap):
    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
