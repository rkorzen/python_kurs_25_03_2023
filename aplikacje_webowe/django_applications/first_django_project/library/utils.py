import csv
from typing import List

from faker import Faker

from library.models import Author, Book


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


def search_books(q: str):
    books = Book.objects.filter(title__icontains=q)

    for book in books:
        print(f"Tytuł: {book.title}, Author: {book.author.name} {book.author.surname}")


def generate_fake_authors(n: int) -> List[Author]:
    fake = Faker("pl_PL")
    authors = []
    for _ in range(n):
        b_year = fake.random_int(min=1900, max=2020)
        years_of_life = fake.random_int(min=0, max=120)
        row = [fake.first_name(), fake.last_name(), b_year, b_year + years_of_life]
        authors.append(create_author(row))
    return authors

def generate_fake_books(n: int) -> List[Book]:
    fake = Faker("pl_PL")
    authors = Author.objects.all()
    books = []
    for _ in range(n):
        author = fake.random_element(elements=authors)
        row = {
            "title": fake.text(max_nb_chars=50),
            "author": author,
            "year": fake.random_int(min=1900, max=2020),
            "pages": fake.random_int(min=10, max=1000),
            "price": fake.random_int(min=10, max=1000),
        }
        books.append(create_book(row))