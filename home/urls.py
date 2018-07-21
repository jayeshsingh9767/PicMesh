from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.home, name='home'),                                 # home
    url(r'^details/(?P<photo_id>[0-9]+)/$', views.details, name='details'),    # home/<photo_id>
    url(r'^categories/(?P<cat_id>[0-9]+)/$', views.categories, name='categories'),
    path('collection/', views.collection, name='collection')

]

