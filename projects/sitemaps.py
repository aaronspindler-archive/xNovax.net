from django.contrib.sitemaps import Sitemap

from .models import Project


class ProjectSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return Project.objects.all()
