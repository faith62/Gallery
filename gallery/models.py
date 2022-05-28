from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


