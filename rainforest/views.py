from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product, ProductForm


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)