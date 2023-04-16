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
    pass