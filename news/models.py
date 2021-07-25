from typing import Text
from django.db import models
from datetime import date, datetime

from django.db.models.fields import BLANK_CHOICE_DASH


class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
