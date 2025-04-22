from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")

def about_us(request):
    return render (request, "home/about_us.html")