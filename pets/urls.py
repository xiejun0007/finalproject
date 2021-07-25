from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='pets'),
    path('news/', include('news.urls')),
    path('search', views.search, name='search'),
    path('searchpet', views.searchpet, name='searchpet'),
    path('<int:pet_id>', views.pet, name='pet'),
    path('aboutpets', views.aboutpets, name='aboutpets'),
]
