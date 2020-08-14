from django.contrib.sitemaps import Sitemap

from .models import Book


class BookSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return Book.objects.all()
