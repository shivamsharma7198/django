from django.db import models
from django.urls import reverse
# Create your models here.
class Cosmos(models.Model):
    planetary_body = models.CharField(max_length = 20)
    category       = models.CharField(max_length = 20)
    distance       = models.CharField(max_length = 100)
    moons          = models.CharField(max_length = 20)
    def get_absolute_url(self):
        return reverse('cosmic-list')