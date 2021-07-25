from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='pets'),
    path('news/', include('news.urls')),
    path('search', views.search, name='search'),
    path('aboutpets', views.aboutpets, name='aboutpets'),
    #path('<int:peoples_id>', views.person, name='person')
]
