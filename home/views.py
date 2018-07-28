import zipfile

from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.template import loader
from django.contrib.auth import get_user
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

trending_pics = all_photos[5:10]

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
    'trending_pics': trending_pics
}


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def details(request, photo_id):
    template = loader.get_template('details.html')
    if request.user.is_authenticated:
        photo = get_object_or_404(Photo, pk=photo_id)
        collected_pic = Coll.objects.filter(user=request.user, photo=photo_id)
        context['photo_id'] = photo_id
        context['photo'] = photo
        if request.method == 'POST':
            if not collected_pic:
                p = Photo.objects.get(id=photo_id)
                c = Coll(user=request.user, photo=p)
                c.save()
                context['button_text'] = 'Remove From Collection'
                return HttpResponse(template.render(context, request))
            else:
                p = Photo.objects.get(id=photo_id)
                Coll.objects.filter(user=request.user, photo=p).delete()
                context['button_text'] = 'Add to Collection'
                return HttpResponse(template.render(context, request))
        context['button_text'] = 'Add to Collection'
        if collected_pic:
            context['button_text'] = 'Remove From Collection'
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


def categories(request, cat_id):
    cat_obj = get_object_or_404(Categories, pk=cat_id)
    cat_pics = Photo.objects.filter(category=cat_id)
    template = loader.get_template('category.html')
    context['catObject'] = cat_obj
    context['catPics'] = cat_pics
    return HttpResponse(template.render(context, request))


def collection(request):
    template = loader.get_template('collection.html')
    if request.user.is_authenticated:
        coll = Coll.objects.filter(user=request.user)
        # col_pic = Photo.objects.filter(id=coll.user)
        ids = Coll.objects.values_list('photo', flat=True).filter(user=request.user)
        col_pic = Photo.objects.filter(id__in=set(ids))

        context['col_pic'] = col_pic
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))






