from django.db import models


# Create your models here.

class Data(models.Model):
    rok = models.IntegerField()
    miesiac = models.IntegerField()
    wartosc = models.FloatField()
    data_importu = models.DateTimeField()

    def __str__(self):
        return f"{self.rok} {self.miesiac} {self.wartosc} {self.data_importu}"
