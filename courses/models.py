from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    instituition = models.CharField(max_length=500)
    course_code = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    external_link = models.URLField(null=True, blank=True)
    certificate_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
