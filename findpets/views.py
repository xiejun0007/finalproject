from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Findpets

def index(request):
    return render(request, 'pages/index')

def findpets(request):
    return render(request, 'findpets/findpets.html')

def findpet(request):
    name = request.POST['name']
    weight = request.POST['weight']
    gender = request.POST['gender']
    location = request.POST['location']
    categories = request.POST['categories']
    image = request.POST['image']

    findpets = Findpets(name=name, weight=weight, gender=gender,location=location, categories=categories,image=image)
    findpets.save()
    return render(request, 'findpets/findpets.html')