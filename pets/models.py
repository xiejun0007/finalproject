from django.db import models
from datetime import datetime
# Create your models here.
class Pets(models.Model):
    name=models.CharField(max_length=200)
    weight=models.IntegerField()
    gender=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    province=models.CharField(max_length=200)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    poster_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name