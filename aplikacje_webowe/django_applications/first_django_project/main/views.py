from django.http import HttpResponse
from django.shortcuts import render

class Person:
    def __init__(self, name, age):
        self.nane=name,
        self.age=age


def hello_view(request, greetings="Hello", name="World!"):
    greeting = greetings.upper()
    n = name.capitalize()

    return render(
        request=request,
        template_name="main.html",
        context={
            "text": f"{greeting} {n}",
            "imiona": ["Adam", "Piotr"],
            "slownik": {"ala": "pies"},
            "obiekt": Person("Maciek", 19)
        }
    )