from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image, ImageDraw, ImageFont


# Create your models here.

# Algorithm for adding Watermark to Image
def watermark_image_with_text(filename):
    print(filename)
    if ".TIF" in str(filename):
        print('error Occoured')
        raise ValidationError("Error ")
    else:
        print('Alright')
        text = 'PicMesh'
        color = 'blue'
        fontfamily = 'arial.ttf'
        image = Image.open(filename).convert('RGBA')
        imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(imageWatermark)
        width, height = image.size
        font = ImageFont.truetype(fontfamily, int(height / 20))
        textWidth, textHeight = draw.textsize(text, font)
        x = width / 5
        y = height / 6
        draw.text((x, y), text, color, font)
        my_image = Image.alpha_composite(image, imageWatermark)
        my_image.convert('RGB').save('D:\Github\PicMesh\media\water_'+filename.name + '.png')
        return 'D:\Github\PicMesh\media\water_'+filename.name + '.png'


class Photo(models.Model):
    format_of_tags = (
        ('PNG', 'PNG'),
        ('JPG', 'JPG'),
        ('JPEG', 'JPEG'),
        ('Exif', 'Exif'),
        ('TIF', 'TIF'),
        ('GIF', 'GIF'),
        ('WEBP', 'WEBP'),
        ('SVG', 'SVG'),
    )
    title = models.CharField(max_length=150)
    format = models.CharField(max_length=20, choices=format_of_tags, blank=False)
    tags = models.CharField(max_length=250)
    original_pic = models.ImageField()
    display_pic = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    photographer = models.ForeignKey('Photographer', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=0)

    # Overwrites save method and set value of display_pic by default
    def save(self, *args, **kwargs):
        print(self.original_pic)
        if not self.pk:
            rotate_img_name = watermark_image_with_text(self.original_pic)
        else:
            rotate_img_name = self.display_pic
        self.display_pic = rotate_img_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title   # this Function adds name as Given Title


class Photographer(models.Model):
    photographer_name = models.CharField(max_length=150)
    profile_pic = models.ImageField(default='default-profile.png')
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


class Coll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.photo.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, unique=False)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user)







