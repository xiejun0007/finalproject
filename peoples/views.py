from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Person

def index(request):

    peoples = Person.objects.all()
    paginator = Paginator(peoples, 6)
    page = request.GET.get('page')
    paged_peoples = paginator.get_page(page)

    context= {
        'peoples' : paged_peoples
    }

    return render(request, 'peoples/peoples.html', context)

def person(request, person_id):

    person = get_object_or_404(Person, pk=person_id)

    context = {
        'person': person
    }

    return render(request, 'peoples/person.html', context)

def findpeople(request):
    return render(request,'findpeople/findpeople.html')

def aboutpeoples(request):
    return render(request, 'pages/aboutpeoples.html')

def searchperson(request):
    
    queryset_list = Person.objects.all()
        
    #name
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
              name__icontains=keywords) 
    #age
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            queryset_list = queryset_list.filter(
              age__iexact=age)
    #weight
    if 'weight' in request.GET:
        weight = request.GET['weight']
        if weight:
            queryset_list = queryset_list.filter(
              weight__iexact=weight)                            
    #height
    if 'height' in request.GET:
        height = request.GET['height']
        if height:
            queryset_list = queryset_list.filter(
              height__iexact=height)          
   
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
              state__iexact=state) 
                                
    context = {
        'values':request.GET,
        'peoples': queryset_list
    
    }
            
    return render(request,'peoples/searchperson.html', context)
            