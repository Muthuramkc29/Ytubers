from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):

    category_choices = (
        ('Code', 'Code'),
        ('Mobile_review','Mobile_review'),
        ('Gaming','Gaming'),
        ('Vlogs', 'Vlogs'),
        ('Cooking', 'Cooking'),
        ('Comedy', 'Comedy')
    )

    crew_choices = (
        ('Solo', 'Solo'),
        ('Small', 'Small'),
        ('Large', 'Large')
    )

    camera_choices = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Fujji', 'Fujji'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/')
    category = models.CharField(choices=category_choices, max_length=255)
    subs_count = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    price = models.IntegerField()
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

