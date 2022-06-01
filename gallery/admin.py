from django.contrib import admin
from .models import Image,Category,Location

# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)

admin.site.site_header='Gallery-Photo admin'
admin.site.site_title='GP'
admin.site.index_title='Welcome to Gallery-Photo admin'