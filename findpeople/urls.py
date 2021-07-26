from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='findpeople'),
    path('findpeople', views.findpeople, name='findpeople'),
    path('findperson', views.findperson, name='findperson'),
    path('insertinfo', views.insertinfo, name='insertinfo')
]

