# Generated by Django 3.1 on 2020-09-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planetary_body', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('distance', models.CharField(max_length=100)),
                ('moons', models.CharField(max_length=20)),
            ],
        ),
    ]
