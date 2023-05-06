from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey("library.Author", on_delete=models.CASCADE, related_name="books")
    year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Author(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
