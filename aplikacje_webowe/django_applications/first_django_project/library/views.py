from django.shortcuts import render
from django.db.models import Q
from library.models import Author, Book


# Create your views here.
def authors_list(request):

    q = request.GET.get("q")

    if not q:
        authors = Author.objects.all()
    else:
        authors = Author.objects.filter(Q(name__icontains=q) | Q(surname__icontains=q))

    return render(request, "library/authors_list.html", {"authors": authors})

def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(request, "library/author_details.html", {"author": author})

def books_list(request):
    q = request.GET.get("q")

    if not q:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(title__icontains=q)

    return render(request, "library/books_list.html", {"books": books})

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, "library/book_details.html", {"book": book} )
