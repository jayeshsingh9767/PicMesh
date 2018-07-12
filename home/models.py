from django.db import models

# Create your models here.


class Photos(models.Model):
    title = models.CharField(max_length=150)
    format = models.CharField(max_length=20)
    tags = models.CharField(max_length=250)
    original_pic = models.ImageField(upload_to='photos/', blank=False)
    description = models.CharField(max_length=1000)
    photographer = models.ForeignKey('Photographer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # this Function adds name as Given Title


class Photographer(models.Model):
    photographer_name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    email_id = models.EmailField()
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.photographer_name  # this Function adds name as Given Name of Photographer







