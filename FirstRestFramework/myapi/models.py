from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50, verbose_name='Character Name')
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

