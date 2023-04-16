from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request, greetings="Hello", name="World!"):
    greeting = greetings.upper()
    n = name.capitalize()

    return render(
        request=request,
        template_name="main.html",
        context={
            "text": f"{greeting} {n}"
        }
    )