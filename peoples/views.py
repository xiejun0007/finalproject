from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def peopleshome(request):
    return render(request, 'peoples/peoples.html')