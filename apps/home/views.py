from django.shortcuts import render
from .models import AboutUs

def home(request):
    current_url='asosiy'

    context = {'current_url': current_url}
    return render(request, "home/index.html",context )

def about_us(request):
    bizning_tarix = AboutUs.objects.first()

    current_url='biz-haqimizda'

    context = {'current_url': current_url,
               'bizning_tarix' : bizning_tarix}
    return render (request, "home/about_us.html", context) 