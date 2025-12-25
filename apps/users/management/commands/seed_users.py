from faker import Faker

from django.core.management import BaseCommand

from apps.categories.models import Category
from apps.users.models import User


class Command(BaseCommand):
    help = 'Seed users data'

    def handle(self, *args, **options):
        fake = Faker()
        users = []
        for _ in range(10):
            user = User(email=fake.email())
            user.set_password(fake.password())
            users.append(user)
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 10 users'))
