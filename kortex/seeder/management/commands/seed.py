from django.core.management.base import BaseCommand
from seeder.seed import seed


class Command(BaseCommand):
    help = "This command init app's seeds"

    def handle(self, *args, **options):
        seed()
