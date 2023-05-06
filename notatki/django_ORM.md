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


