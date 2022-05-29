from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def save_editor(self):
        self.delete()

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_location(self):
        self.save()

