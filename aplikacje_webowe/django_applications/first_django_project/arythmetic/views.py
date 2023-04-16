from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .kalkulator import operations



def calculator(request, op, a, b):

    result = operations[op](a, b)

    return render(
        request,
        "arythmetic/main.html",
        {"result": result}
    )

# /maths/cwiczenie/
def cwiczenie_4(request):
    # utwórz liste liczb i przekaż do szablonu
    # w szablonie w pętli wypisz te liczby - każda w osobnej linii
    return render(
        request,
        "arythmetic/cwiczenie4.html",
        {"liczby": list(range(40))}
    )


def kalkulator_v2(request):
    # przyjmie dane z formularza

    a = request.POST.get("a")
    b = request.POST.get("b")


    if a and b:
        a, b = int(a), int(b)
        wynik = a + b
    else:
        wynik = ""


    return render(request, "arythmetic/k2.html", {"wynik": wynik})