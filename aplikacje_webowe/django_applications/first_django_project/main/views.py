from django.http import HttpResponse


def hello_view(request, greetings="Hello", name="World!"):
    greeting = greetings.upper()
    n = name.capitalize()

    return HttpResponse(f"{greeting} {n}")