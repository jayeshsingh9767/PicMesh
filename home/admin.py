from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Photo)
admin.site.register(Photographer)
admin.site.register(Categories)
admin.site.register(Coll)
admin.site.register(Order)

admin.site.site_header = 'PicMesh Administration'
