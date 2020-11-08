from django.db.models import Q, F
from django.shortcuts import render
from .models import Cars
from .forms import CarsForm

# Create your views here.


def cars_list(request):
    search_query = request.GET.get('search', '')
    m_search_dict = request.GET.dict()

    if search_query:
            cars = Cars.objects.filter(Q(mark__icontains=search_query) |
                                      Q(model__icontains=search_query) |
                                      Q(year__iexact=search_query) |
                                      Q(color__icontains=search_query) |
                                      Q(gear__in=[list(n)[0] for n in list(Cars.GEAR_CHOICES) if search_query in list(n)])
                                       )
            message = 'Cars: '

            if cars.count()==0:
                message = 'Машины не найдены!'

    elif m_search_dict:
        cars = Cars.objects.all()
        if m_search_dict['mark']:
            cars = cars.filter(mark__icontains=m_search_dict['mark'])
        if m_search_dict['model']:
            cars = cars.filter(model__icontains=m_search_dict['model'])
        if m_search_dict['year']:
            cars = cars.filter(year__iexact=m_search_dict['year'])
        if m_search_dict['color']:
            cars = cars.filter(color__icontains=m_search_dict['color'])
        if m_search_dict['gear']:
            cars = cars.filter(gear__in=[list(n)[0] for n in list(Cars.GEAR_CHOICES) if m_search_dict['gear'] in list(n)])

        message = 'Cars: '

        if cars.count()==0:
            message = 'Машины не найдены!'

    else:
        cars = Cars.objects.all()
        message = 'Cars: '

    # form = CarsForm()

    return render(request, 'catalog/cars_list.html', context={'cars':cars, 'message': message})
    # return render(request, 'catalog/cars_list.html', context={'cars':cars, 'form':form})
