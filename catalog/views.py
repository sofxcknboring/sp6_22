from django.shortcuts import render
from catalog.models import Product
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            return HttpResponse(f"{name}, {phone}! success!")
        return render(request, 'contact.html')


class ProductDetailView(DetailView):
    model = Product
