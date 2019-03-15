
from .models import Image,Category,Location
from django.http  import Http404
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

def display_location(request,location_id):
    location = Location.objects.get(id = location_id)
    images = Image.objects.filter(location = location.id)
    
    return render(request,'all-images/location.html',{'location':location,'images':images})


def search_category(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'images':searched_images,'locations':locations})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message,'locations':locations})