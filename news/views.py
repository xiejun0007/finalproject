from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import New

def index(request):

    news = New.objects.all()
    paginator = Paginator(news, 6)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)

    context= {
        'news' : paged_news
    }

    return render(request, 'news/news.html', context)

def new(request, new_id):

    new = get_object_or_404(New, pk=new_id)

    context = {
        'new': new
    }

    return render(request, 'news/new.html', context)

def news(request):

    news = New.objects.all()
    paginator = Paginator(news, 6)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)

    context= {
        'news' : paged_news
    }

    return render(request, 'news/news.html', context)