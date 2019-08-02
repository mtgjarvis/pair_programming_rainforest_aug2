from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product, ProductForm


def index(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, "index.html", context)