from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    image_category= models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null = True,)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    
    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__name__icontains=image_category)
        return images

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

