from faker import Faker

from django.core.management import BaseCommand

from apps.categories.models import Category


class Command(BaseCommand):
    help = 'Seed categories data'

    def handle(self, *args, **options):
        fake = Faker()
        categories = []
        for _ in range(50):
            categories.append(Category(name=fake.word()))
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 50 categories'))
