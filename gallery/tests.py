from django.test import TestCase

from .models import Category, Image, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.sushi = Image(name = 'sushi', description= 'a Japanese dish consisting of small balls or rolls of vinegar-flavoured cold rice served with a garnish of vegetables, egg, or raw seafood.')
        self.sushi.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

