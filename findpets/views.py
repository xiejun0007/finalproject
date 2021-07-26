from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Findpets

def index(request):
    return render(request, 'pages/index.html')

def findpets(request):
    # print('FINDPET!!!!!!!!!!!!!!!!!!!!!!!!!11')
    queryset_list=Findpets.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list=queryset_list.filter(
                name__icontains=name
            )

    if 'weight' in request.GET:
        weight = request.GET['weight']
        if weight:
            queryset_list=queryset_list.filter(
                weight__lte=weight
            )
            
    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list=queryset_list.filter(
                gender__iexact=gender
            )

    if 'categories' in request.GET:
        category = request.GET['categories']
        if category:
            queryset_list=queryset_list.filter(
                category__iexact=category
            ) 

    if 'location' in request.GET:
        province = request.GET['location']
        if province:
            queryset_list=queryset_list.filter(
                province__iexact=province
            )  

    context = {
        'values': request.GET,
        'findpets': queryset_list
    }
    return render(request, 'findpets/findpets.html', context)

def findpet(request):
    return render(request, 'findpets/insertinfopets.html')

def insertinfopets(request):
    # print('11111111111111111')
    name = request.POST.get('name')
    weight = request.POST.get('weight')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    location = request.POST.get('location')
    categories = request.POST.get('categories')
    image = request.POST.get('image')
    findpets = Findpets(name=name, weight=weight,age=age, gender=gender, location=location, categories=categories, image=image)
    findpets.save()
    return redirect('findpets')