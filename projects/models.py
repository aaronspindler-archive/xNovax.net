from django.db import models
from django.urls import reverse
from django.utils import timezone


class Technology(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=140, blank=True)
    description = models.TextField()
    github_link = models.URLField(null=True, blank=True)
    deployment_link = models.URLField(null=True, blank=True)
    technologies = models.ManyToManyField('Technology')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.pk)])

    class Meta:
        ordering = ['-created_at']
