from django.db import models
from datetime import date, datetime

from django.db.models.fields import BLANK_CHOICE_DASH


class Findpets(models.Model):
    name = models.CharField(max_length=200)
    weight=models.IntegerField()
    age= models.IntegerField()
    gender=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    categories=models.CharField(max_length=100)
    image = models.ImageField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
