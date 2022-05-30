from django.shortcuts import render
from django.http  import HttpResponse

from .models import Image

# Create your views here.
def welcome(request):
    images = Image.get_all_images()

    return render(request,'welcome.html',{"images":images})
# Create your views here.


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        image_category = request.GET.get("image")
        searched_images = Image.search_by_category(image_category)
        message = f"{image_category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})