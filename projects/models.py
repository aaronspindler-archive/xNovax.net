from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=140, blank=True)
    description = models.TextField()
    github_link = models.URLField(null=True, blank=True)
    deployment_link = models.URLField(null=True, blank=True)
    technologies = models.ManyToManyField('Technology')

    def __str__(self):
        return self.title
