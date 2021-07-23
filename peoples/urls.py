from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='peoples'),
    path('peopleshome', views.peopleshome, name='peopleshome'),
    #path('about', views.about, name='about'),
    #path('<int:peoples_id>', views.person, name='person')
]
