# Generated by Django 3.1 on 2020-12-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
