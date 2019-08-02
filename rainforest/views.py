from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product, ProductForm

def root(request):
    return HttpResponseRedirect("index")

def index(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, "index.html", context)

def show(request, id):
    product = Product.objects.get(pk=id)
    context = {"product": product}
    return render(request, "show.html", context)