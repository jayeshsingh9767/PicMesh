from django.shortcuts import render,HttpResponse
from .models import *
from django.template import loader
# Create your views here.


def cat_name(cname):
    return cat.get(category_name=cname)


all_photos = Photo.objects.all()
cat = Categories.objects.all()
auther = Photographer.objects.all()
city_pic = Photo.objects.filter(category=cat.get(category_name='City'))
nature_pic = Photo.objects.filter(category=cat.get(category_name='Nature'))
brand_pic = Photo.objects.filter(category=cat.get(category_name='Brand Logo'))[:5]
devotion_pic = Photo.objects.filter(category=cat.get(category_name='Devotional'))
back_pic = Photo.objects.filter(category=cat.get(category_name='Background'))
mountain_pic = Photo.objects.filter(category=cat.get(category_name='Mountains'))
animal_pic = Photo.objects.filter(category=cat.get(category_name='Animals'))

context = {
    'all_photos': all_photos,
    'cat': cat,
    'auther': auther,
    'city_pic': city_pic,
    'brand_pic': brand_pic,
    'nature_pic': nature_pic,
    'devotion_pic': devotion_pic,
    'back_pic': back_pic,
    'mountain_pic': mountain_pic,
    'animal_pic': animal_pic,
    'cat_name_city': cat_name('City'),
    'cat_name_nature': cat_name('Nature'),
    'cat_name_animal': cat_name('Animals'),
    'cat_name_mountain': cat_name('Mountains'),
    'cat_name_brand': cat_name('Brand Logo'),
    'cat_name_devotion': cat_name('Devotional'),
}


def home(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render(context, request))


def details(request, photo_id):
    template = loader.get_template('details.html')
    context['photo_id'] = photo_id
    return HttpResponse(template.render(context, request))


