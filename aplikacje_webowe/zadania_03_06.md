# ImageField

## Zadanie 1

- Utwórz projekt "examples"
- Utwórz aplikację "books"
- Utwórz model "Book" z polami:

  - title
  - author
  - description
  - published_at
  - cover_image  (ImageField, pip install Pillow, ustwić MEDIA_ROOT, MEDIA_URL, zmodifikować urls.py)

- Utwórz migrację
- Dodaj model do panelu admina
- Sprawdź czy dodany obrazek się wyświetla (po utworzeniu książki w panelu admina)

## zadanie 2

Doda miniaturki obrazków w liście 

## Zadanie 3

Import danych z pliku CSV i zrobienie wykresów

## Zadanie 4

Utwórz model do którego możesz zaimportowa dane z pliku csv
Pola to: rok, miesiac, wartosc, data_importu

## Zadanie 5

Formularz - forms.Form
utwórz formularz dla ksiązki
Zadba o to by tytuł był zapisywany z dużej litery
Podobnie dla autora (imie i nazwisko z dużej litery)
odpal shell i sprawdź czy działa poprawnie 

form = MyForm(data={"slownik z danymi"})
form.data
form.is_valid()
form.cleaned_data

form.errors


## Zadanie 6

utwórz aplikację "blog"
utwórz model "Post" z polami:
author - relacja z auth.User
title 
content
created_at
updated_at

utwórz migrację
wykonaj migrację

utwórz formularz dla modelu Post (forms.ModelForm)

utwórz widok post_list, który wyświetli wszystkie posty i który umożliwia
utworzenie nowego posta - w szablonei i widoku posługuj się formularzem


instance = form.save(commit=False)
instance.author = request.user


## zadanie 7

Korzystając z Crispy Forms zmodyfikuj widok listy książek - tak by można było dodać nową książkę
Zmodifikuj widok szczegółów ksiażki tak by można było edytować książkę
Doda widok modyfikacji posta


