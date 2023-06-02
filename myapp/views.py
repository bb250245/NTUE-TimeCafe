from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def Order(request):
    return render(request, 'Order.html')

def Login(request):
    return render(request, 'Login.html')
