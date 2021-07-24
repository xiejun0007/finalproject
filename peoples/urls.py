from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='peoples'),
    path('peoples', views.peoples, name='peoples'),
    path('aboutpeoples', views.aboutpeoples, name='aboutpeoples')
]
