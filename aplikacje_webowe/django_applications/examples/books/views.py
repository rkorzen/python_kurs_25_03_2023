from django.shortcuts import render
from books.models import Book
# Create your views here.


def books_list(request):
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "books/details.html", {"book": book})

