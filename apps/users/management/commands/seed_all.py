from faker import Faker

from django.core.management import BaseCommand, call_command

from apps.categories.models import Category


class Command(BaseCommand):
    help = 'Seed data...'

    def handle(self, *args, **options):
        seed_commands = [
            'seed_users',
            'seed_categories',
            'seed_products',
        ]

        for command in seed_commands:
            call_command(command)
        self.stdout.write(self.style.SUCCESS('Successfully seeded!!'))
