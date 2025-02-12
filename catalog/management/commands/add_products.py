from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="Обувь",)

        products = [
            {'prod_name': 'Кроссовки', 'price': 3000, 'category': category},

        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added sneakers: {product.prod_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'sneakers already exists: {product.prod_name}'))
