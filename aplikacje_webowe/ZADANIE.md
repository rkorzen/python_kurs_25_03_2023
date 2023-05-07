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

## zadanie - dodanie komendy manage.py do dodawania fakeowych ksiażek i autorów

## zadanie - paginator

w oparciu o https://docs.djangoproject.com/en/4.2/topics/pagination/

1. tworzymy paginator w widoku listy książek i listy autorów - przekazujemy do szablonu page_obj
2. zmieniamy szablon by wyświetlał obiekty przekazane jako page_obj

## zadanie - blog


Oto propozycja ćwiczenia związana z napisaniem aplikacji Django typu blog:

1. Stwórz nowy projekt Django o nazwie "blog". 
   `django-admin startproject blog`
2. Dodaj aplikację o nazwie "posts", która będzie zawierała modele `Post` i `Comment`. 
   `python manage.py startapp posts`
3. Dodaj aplikację do listy zainstalowanych aplikacji w pliku `settings.py`.
4. Zdefiniuj model `Post` z polami takimi jak: 
   `title` (tytuł postu), `author` (autor postu - relacja), `content` (treść postu), `created_at` (data utworzenia postu).

```python
    class Post(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)    
```

4. Zdefiniuj model `Comment` z polami takimi jak: `author` (autor komentarza - relacja do auth.User), 
   `content` (treść komentarza), `created_at` (data utworzenia komentarza) i klucz obcy `post` (do którego postu należy dany komentarz).
5. Stwórz widok `post_list`, który będzie wyświetlał listę wszystkich postów wraz z ich tytułami, autorami i datami utworzenia. 
6. Stwórz szablon do wyświetlania listy postów- 'posts/post_list.html'.

struktura projektu:
```
    manage.py
    blog
        settings.py
    posts
        models.py
        views.py
        urls.py
        templates
            posts
                post_list.html
                post_detail.html
```
6. Stwórz widok `post_detail`, który będzie wyświetlał szczegóły danego postu, wraz z jego tytułem, autorem, treścią i datą utworzenia. 
7. Utwórz 100 postów (przy pomocy faktera - mozna doda polecenie command)
8. Utwórz stronicowanie dla listy postów
