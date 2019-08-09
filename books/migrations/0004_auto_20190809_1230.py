# Generated by Django 2.2.4 on 2019-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('R', 'Read'), ('CR', 'Currently Reading'), ('N', 'Next to Read'), ('O', 'On List to Read')], default='O', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='favourite_passage',
            field=models.TextField(null=True),
        ),
    ]
