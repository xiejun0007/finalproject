from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news'),
    path('news', views.news, name='news'),
    path('<int:new_id>', views.new, name='new'),
]
