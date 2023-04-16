from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .kalkulator import operations



def calculator(request, op, a, b):

    result = operations[op](a, b)

    return HttpResponse(f"{result}")