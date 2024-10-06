from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.defaultfilters import title
from products.models import ProductCategory,Product

# Create your views here.
def index(request):
    context = {
        'title': 'Store',
        'is_promotion': True

    }

    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
            }
    return render(request, 'products/products.html',context)