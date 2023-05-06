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


def create_book(row: dict):

    book = Book.objects.create(
        **row
    )
    return book

def prepare_book_data(row: dict):
    # title, author_name, author_surname, year, pages, price, author_birth_year
    author, created = Author.objects.get_or_create(name=row["author_name"], surname=row["author_surname"], birth_year=row["author_birth_year"])
    row.pop("author_name")
    row.pop("author_surname")
    row.pop("author_birth_year")

    row["author"] = author

    return row

def import_books():
    with open("data/books.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data = prepare_book_data(row)
            create_book(data)