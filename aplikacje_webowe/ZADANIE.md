# zad 1

utwórz taki wzorzec i taki widok, by powitanie działało tak

/hello/goodmorning/rafał

GOODMORNING Rafał

/hello/hi/rafał

HI Rafał

/hello/bonjorno/pablo

BONJORNO Pablo


# zad 2

1. utworz aplikacje `arythemtic`
2. utworz urls, views, powiąż z głownymi urls
3. zaimplementuj kalkukator oparty o adresy url

/maths/add/1/2/

3

/maths/sub/1/2/

-1

# zad 3

Użyj render do wyrenderowania szablony dla obliczeń

# zad podsumowujace zjazd 2

0. utwórz wirtulne środowisko

workspace - jakiś katalog

W nim:  
python -m venv venv
mac: source venv/bin/activate
win: venv\Scripts\activate
(venv) 

workspace
   venv
   requirements.txt

pip install -r requirements.txt

django-admin startproject waluty .

workspace
   venv
   requirements.txt
   waluty
     settings.py
   manage.py



1. utwórz plik requirements.txt: django, requests
   2. pip install -r requirements.txt
1. utwórz nowy django projekt django-admin startproject ...
2. nowa aplikacja - waluty
3. widok umożliwiajacy przeliczenie wartości waluty - chcemy kupi jakaś walutę ile musimy zapłaci PLN ?
4. dane z API NBP


## Zadanie - modele

* Utwórz aplikację Django o nazwie "Library".
* Stwórz dwa modele: "Author" oraz "Book". Model "Author" będzie zawierał informacje o autorze książki, a model "Book" będzie zawierał informacje o książce, takie jak tytuł, opis, datę publikacji oraz informację o autorze.

   class Book:
      ...
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      ...
* przygotuj i wykonaj migracje
* utwórz kilku autorów
* utwórz kilka książek

   book = Book(..., author=author)

## zadanie - dane

1. W aplikacji library utwórz moduł utils, który będzie zawierał funkcję, która będzie pobierała dane z pliku
<projekt>/data/authors.csv
2. Na podstawie danych utwórz instancje modelu Author
3. Powtórz to dla książek - books.csv i model Book
4. Napisz funkcjonalnoś, która zapewni:
   - wyszukiwanie książek po tytule 
   - wypisanie znalezionych książek w formacie "Tytuł: [tytuł], Autor: [imię] [nazwisko]"

    $ python manage.py shell
    >>> from library.utils import search_books
    >>> search_books('Pan Tadeusz')
    Tytuł: Pan Tadeusz, Autor: Adam Mickiewicz



## zadanie - połączenie widoków, szablonów i modeli.

1. Utwórz widok, który będzie wyświetlał listę książek
2. Utwórz szablon, który będzie wyświetlał listę książek
3. Utwórz widok, który będzie wyświetlał listę autorów
4. Utórz szablon, który będzie wyświetlał listę autorów
5. Utwórz widok, który będzie wyświetlał szczegóły książki
6. Utwórz szablon, który będzie wyświetlał szczegóły książki
7. Utwórz widok, który będzie wyświetlał szczegóły autora wraz z listą jego książek

8. Utwórz prosty formularz do wyszukiwania książek po tytule

## zadanie - funcja do generowania fakeowych ksiażek i autorów
Dwie funkcje. Tworząc książkę wybieraj autora z istniejących autorów

## zadanie - odanie komendy manage.py do dodawania fakeowych ksiażek i autorów