from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Calculation(models.Model):

    OPERATIONS = [
        ("add", "add"),
        ("sub", "sub"),
        ("mul", "mul"),
        ("div", "div"),
    ]

    a = models.IntegerField()
    b = models.IntegerField()
    op = models.CharField(max_length=4, choices=OPERATIONS, validators=[MinLengthValidator(3)]) # add, sub, mul, div, pow, sqrt
    result = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)