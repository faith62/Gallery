from django.contrib import admin
from .models import Image,Category,Location

class ImageAdmin(admin.ModelAdmin):    
   
    list_display = ('name', 'pic')

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)

admin.site.site_header='Gallery-Photo admin'
admin.site.site_title='GP'
admin.site.index_title='Welcome to Gallery-Photo admin'