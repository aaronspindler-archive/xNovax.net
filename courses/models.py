from django.db import models
from django.urls import reverse


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    instituition = models.CharField(max_length=500)
    course_code = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    external_link = models.URLField(null=True, blank=True)
    certificate_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-created_at']