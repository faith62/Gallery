from django.test import TestCase
from models import Image,Category, Location

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Image(name = 'sishi', description='Japanese dish of prepared vinegared rice', )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sushi,Image))

        # Testing Save Method
    def test_save_method(self):
        self.sushi.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)