# Django ORM

## 1. Wstęp

### Wprowadzenie do ORM i jego rola w Django

### Omówienie relacyjnych baz danych

### Przgląd modeli i ich struktuy

### Praca z migracjami i bazami

przydatne polecenia

```bash
python manage.py makemigrations   # tworzenie migracji
python manage.py migrate          # wykonanie migracji

python manage.py sqlmigrate       # pokazuje sql migracji
python manage.py showmigrations   # pokazuje migracje

python manage.py inspecdb        # tworzy modele na podstawie bazy danych
```

## Tworzenie i modyfikowanie instancji modeli - wpisów do bazy danych

### Tworzenie instancji modeli

#### sposób 1 - save na instancji

```python
c = Calculation(a=2, b=3, op="add")
c.save()
```

#### sposób 2 - create na managerze

```python


### Rodzaje relacji

#### OneToOneField

```
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)

class MyModelDetails(models.Model):
    my_model = models.OneToOneField(MyModel, on_delete=models.CASCADE)
    description = models.TextField()
```

#### ForeignKey

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

#### ManyToManyField

```python
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
class Article(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
```

```

#### on_delete- możliwe wartosci

* CASCADE - usuwa powiązane obiekty
* PROTECT - nie pozwala na usunięcie obiektu, dopóki nie zostaną usunięte powiązane obiekty
* SET_NULL - ustawia wartość null w polu klucza obcego
* SET_DEFAULT - ustawia wartość domyślną w polu klucza obcego
* SET() - ustawia wartość podaną w argumencie
* 