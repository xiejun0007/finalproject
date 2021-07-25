from django.urls import path
from . import views

urlpatterns = [
    path('peoples', views.index, name='findpeople'),
    path('findpeople', views.findpeople, name='findpeople'),
]
