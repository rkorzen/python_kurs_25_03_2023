from django.core.management.base import BaseCommand

from library.utils import generate_fake_books


class Command(BaseCommand):
    help = "Add n books"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="liczba powtórzeń")

    def handle(self, *args, **options):
        n = options["n"]
        generate_fake_books(n)
        print(f"Added {n} books")