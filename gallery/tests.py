from django.test import TestCase

from .models import Category, Image, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.sushi = Image(name = 'sushi', description= 'a Japanese dish consisting of small balls or rolls of vinegar-flavoured cold rice served with a garnish of vegetables, egg, or raw seafood.')
        self.sushi.save_image()    

    def test_instance(self):
        self.assertTrue(isinstance(self.sushi,Image))
    # Testing Save Method
    def test_save_method(self):
        self.sushi.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.sushi.save_image() 
        self.sushi.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)

class CategoryTestClass(TestCase):

    def setUp(self):
        self.technology = Image(name = 'technology', )
        self.technology.save_category()
  
    def test_instance(self):
        self.assertTrue(isinstance(self.technology,Category))
    # Testing Save Method
    def test_save_method(self):
        self.technology.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)

    
    def test_delete_method(self):
        self.technology.save_category() 
        self.technology.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class LocationTestClass(TestCase):

    def setUp(self):
        self.Africa = Location(name = 'Africa', )
        self.Africa.save_location()
  
    def test_instance(self):
        self.assertTrue(isinstance(self.Africa,Location))
    # Testing Save Method
    def test_save_method(self):
        self.Africa.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.Africa.save_location() 
        self.Africa.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
    
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()