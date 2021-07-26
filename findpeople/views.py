from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Findpeople

def index(request):
    return render(request, 'pages/index.html')

def findpeople(request):
    queryset_list=Findpeople.objects.all()

    if 'keywords' in request.GET:
        name = request.GET['keywords']
        if name:
            queryset_list=queryset_list.filter(
                name__icontains=name
            )
    if 'state' in request.GET:
        province = request.GET['state']
        if province:
            queryset_list=queryset_list.filter(
                province__iexact=province
            )  

    context = {
        'values': request.GET,
        'findpeoples': queryset_list
    }
    return render(request, 'findpeople/findpeople.html', context)

def findperson(request):
    print('111111111111111111111')
    return render(request, 'findpeople/insertinfo.html')

def insertinfo(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    # gender = request.POST.get('gender')
    state = request.POST.get('state')
    image = request.POST.get('image')
    findpeoples = Findpeople(name=name, age=age, state=state, image=image)
    findpeoples.save()
    return redirect('findpeople')