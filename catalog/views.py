from django.shortcuts import render
from catalog.models import Product
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)
from catalog.forms import ProductForm
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            name = self.request.POST.get("name")
            phone = self.request.POST.get("phone")
            return HttpResponse(f"{name}, {phone}! success!")
        return render(request, "contact.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")
