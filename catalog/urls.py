from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactTemplateView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
]
