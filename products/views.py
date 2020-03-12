from django.shortcuts import render
from django.http import HttpResponse
from .models import product

def index(request):
    products = product.objects.all()
    return render(request, 'index.html', 
         {'products': products})

def new(request):
    return HttpResponse('new Product')    
