from django.core.management.base import BaseCommand

from library.utils import generate_fake_authors


class Command(BaseCommand):
    help = "Add n authors"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="liczba powtórzeń")

    def handle(self, *args, **options):
        n = options["n"]
        generate_fake_authors(n)
        print(f"Added {n} authors")