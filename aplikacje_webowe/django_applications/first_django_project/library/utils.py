import csv

from library.models import Author, Book
import os

print(os.getcwd())

def hello_django():
    print("Hello Django!")


def create_author(row):
    name, surname, birth_year, death_year = row
    author = Author.objects.create(
        name=name, surname=surname, birth_year=birth_year, death_year=death_year
    )
    return author

def import_authors():
    with open("data/authors.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            create_author(row)
