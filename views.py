from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from azuremoon.models import Product
import json

# Create your views here.

def homepage(request):
    return render(request, "azuremoon/home.html", {})

def get_products_serialized(products):
    data = [p.products_serialized() for p in products]
    return HttpResponse(json.dumps(data), mimetype='application/json')

def view_all_products(products):
    return get_products_serialized(products)

def get_all_products(extension='json'):
    models = Product.objects.all()
    return view_all_products(models)