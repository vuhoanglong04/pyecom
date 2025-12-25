import random

from django.core.management import BaseCommand
from faker import Faker

from apps.categories.models import Category
from apps.products.models import Product


class Command(BaseCommand):
    help = 'Seed products data'

    def handle(self, *args, **options):
        fake = Faker()
        products = []
        for _ in range(50):
            products.append(Product(title=fake.building_number(),
                                    description=fake.text(),
                                    category=random.choice(Category.objects.all()),
                                    price=fake.random_number(digits=3),
                                    ))
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 50 products'))
