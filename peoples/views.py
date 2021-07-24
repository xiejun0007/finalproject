from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def peoples(request):
    return render(request, 'peoples/peoples.html')

def aboutpeoples(request):
    return render(request, 'pages/aboutpeoples.html')
