from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'pages/index')

def findpeople(request):
    return render(request, 'findpeople/findpeople.html')
