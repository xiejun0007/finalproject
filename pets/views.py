from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pets.choices import gender_choices, province_choices, category_choices
from .models import Pets



def news(request):
    return render(request, 'news/news.html')

def search(request):
    print('TestingSearch')
    queryset_list = Pets.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(
                name__icontains=name
            )

    if 'weight' in request.GET:
        weight = request.GET['weight']
        if weight:
            queryset_list = queryset_list.filter(
                weight__lte=weight
            )

    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list = queryset_list.filter(
                gender__iexact=gender
            )

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(
                category__iexact=category
            )

    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset_list = queryset_list.filter(
                category__iexact=province
            )

    context = {
        'gender_choices': gender_choices,
        'category_choices': category_choices,
        'province_choices': province_choices,
        'pets': queryset_list,
        # 'pets_id': pets_id
    }
    return render(request, 'pets/search.html',context)


def aboutpets(request):
    return render(request, 'pages/aboutpets.html')

def searchpet(request):
    print('Testing Searchpet')
    queryset_list=Pets.objects.all()

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

    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset_list=queryset_list.filter(
                province__iexact=province
            )  

    context = {
        'gender_choices':gender_choices,
        'category_choices':category_choices,
        'province_choices':province_choices,
        'pets': queryset_list
    }

    return render(request, 'pets/searchpet.html',context)


def index(request):
    pets = Pets.objects.order_by('-list_date')
    paginator = Paginator(pets, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'searchpet': paged_listings
    }
    return render(request, 'search/searchpet.html',context)

def pet(request, pet_id):
    print('Testingpetsinfo')
    pet=get_object_or_404(Pets,pk=pet_id)

    context={
        'pet':pet,
    }
    return render(request,'pets/petsinfo.html', context)

def findpets(request):
    return render(request,'findpets/findpets.html')