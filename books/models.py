from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    purchase_link = models.URLField(null=True, blank=True)
    favourite_passage = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title;
