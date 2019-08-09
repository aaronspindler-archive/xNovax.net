from django.db import models

class Book(models.Model):

    STATUS_CHOICES = (
    ('R','Read'),
    ('CR','Currently Reading'),
    ('N','Next to Read'),
    ('O','On List to Read'),
    )

    title = models.CharField(max_length=500)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='O')
    subtitle = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    purchase_link = models.URLField(null=True, blank=True)
    favourite_passage = models.TextField(null=True)
    cover = models.ImageField(upload_to='book/')

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title;