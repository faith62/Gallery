from django.db import models

from pyuploadcare.dj.models import ImageField

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    image_category= models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null = True,)
    pic = models.ImageField(upload_to = 'images/',blank=True,null = True)
    image_location= models.ForeignKey('Location',on_delete=models.CASCADE,blank=True,null = True,)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.pic: #check if image exists before resize
            img = Image.open(self.pic.path)

            if img.height > 1080 or img.width > 1920:
                new_height = 720
                new_width = int(new_height / img.height * img.width)
                img = img.resize((new_width, new_height))
                img.save(self.pic.path)

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

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

