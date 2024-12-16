from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        electronics = Category.objects.create(name='Electronics')
        books = Category.objects.create(name='Books')

        Product.objects.create(name='Laptop', price=1000, category=electronics)
        Product.objects.create(name='Smartphone', price=500, category=electronics)
        Product.objects.create(name='Django Book', price=30, category=books)

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены!'))