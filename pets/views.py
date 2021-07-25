from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

def index(request):
    return 
    # render(request, 'news/news.html')

def news(request):
    return render(request, 'news/news.html')

def search(request):
    return render(request, 'pets/search.html')

def aboutpets(request):
    return render(request, 'pages/aboutpets.html')