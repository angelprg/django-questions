from django.core.management.base import BaseCommand
from app.utils import populate_app


class Command(BaseCommand):
    help = 'Populate the app'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        populate_app.populate()
