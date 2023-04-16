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
