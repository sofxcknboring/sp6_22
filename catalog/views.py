from django.shortcuts import render
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def contacts(request):
    return render(request, "contacts.html")


def products_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
