from django.shortcuts import render,HttpResponse
from .models import Photos
from django.template import loader
# Create your views here.


def home(request):
    all_photos = Photos.objects.all()
    template = loader.get_template('home.html')
    context = {
        'all_photos': all_photos,
    }

    return HttpResponse(template.render(context, request))
