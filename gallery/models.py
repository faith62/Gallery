from django.db import models


from pyuploadcare.dj.models import ImageField

# Create your models here.
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


class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    image_category= models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null = True,)
    pic = models.ImageField(upload_to = 'images/',blank=True,null = True)
    image_location= models.ForeignKey('Location',on_delete=models.CASCADE,blank=True,null = True,)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)
 
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_image_category(cls,search_term):
        gallery = cls.objects.filter(image_category__image_category__icontains=search_term)
        return gallery

    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(image_location__id=image_location)
        return images_location

    class Meta:
        ordering = ['name']


