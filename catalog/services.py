from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product

def get_products_from_caches():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products