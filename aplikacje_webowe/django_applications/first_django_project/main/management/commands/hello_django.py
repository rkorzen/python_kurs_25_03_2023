from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello Django!"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="liczba powtórzeń")

    def handle(self, *args, **options):
        n = options["n"]
        for i in range(n):
            print("Hello Django!")