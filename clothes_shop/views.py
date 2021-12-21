from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.filter()
    context = {
        'products': products
    }
    return render(request, 'templates/home.html', context)