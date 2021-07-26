from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Findpeople

def index(request):
    return render(request, 'pages/index.html')

def findpeople(request):
    return render(request, 'findpeople/findpeople.html')

def findperson(request):
    name = request.POST['name']
    state = request.POST['state']
    age = request.POST['age']
    image = request.POST['image']

    findpeople = Findpeople(name=name, state=state, age=age,image=image)
    findpeople.save()
    return render(request, 'findpeople/findpeople.html')
