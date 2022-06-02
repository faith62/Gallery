from django.shortcuts import render
from django.http  import Http404, HttpResponse
from django.views.generic import ListView, CreateView 
from .models import Category, Image, Location

# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    
    return render(request,'welcome.html',{"images":images})
# Create your views here.


def search_results(request):

    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET["image_category"]:
        search_term = request.GET.get("image_category")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        print(search_term)
        print(searched_images)

        return render(request, 'search.html',{"message":message,"images": searched_images, "categories":categories,'locations':locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,pk):
    try:
        image = Image.objects.get(pk)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

class ImageListView(ListView):
    model = Image
    template_name = 'myapp/image_list.html'

    def get_queryset(self):
        return Image.objects.all()

class ImageCreate(CreateView):
    model = Image
    fields = ['pic','name', 'description','image_category','image_location']
    success_url = '/'