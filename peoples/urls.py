from django.urls import path, include
from . import views

urlpatterns = [
    path('peoples', views.index, name='peoples'),
    path('<int:person_id>', views.person, name='person'),
    path('searchperson', views.searchperson, name= 'searchperson'),
    path('findpeople', include('findpeople.urls')),
    path('aboutpeoples', views.aboutpeoples, name='aboutpeoples'),
]
