from django.shortcuts import render

def home(request):
    current_url='asosiy'

    context = {'current_url': current_url}
    return render(request, "home/index.html",context )

def about_us(request):
    current_url='biz-haqimizda'

    context = {'current_url': current_url}
    return render (request, "home/about_us.html", context)