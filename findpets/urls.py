from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='findpets'),
    path('findpets', views.findpets, name='findpets'),
    path('findpet', views.findpet, name='findpet')
]
