from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    format_of_tags = (
        ('PNG', 'PNG'),
        ('JPG', 'JPG'),
        ('JPEG', 'JPEG'),
        ('Exif', 'Exif'),
        ('GIF', 'GIF'),
        ('WEBP', 'WEBP'),
        ('SVG', 'SVG'),
    )
    title = models.CharField(max_length=150)
    format = models.CharField(max_length=20, choices=format_of_tags, blank=False)
    tags = models.CharField(max_length=250)
    original_pic = models.ImageField()
    description = models.CharField(max_length=1000)
    photographer = models.ForeignKey('Photographer', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title  # this Function adds name as Given Title


class Photographer(models.Model):
    photographer_name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    email_id = models.EmailField()
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.photographer_name  # this Function adds name as Given Name of Photographer


class Categories(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.category_name


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.OneToOneField('Photo', on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.title







