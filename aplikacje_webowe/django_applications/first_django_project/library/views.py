from django.shortcuts import render
from django.db.models import Q
from library.models import Author, Book
from django.core.paginator import Paginator

# Create your views here.
def authors_list(request):

    q = request.GET.get("q")
    page_number = request.GET.get("page", 1)
    objects_per_page = request.GET.get("per_page", 10)

    if not q:
        authors = Author.objects.all()
    else:
        authors = Author.objects.filter(Q(name__icontains=q) | Q(surname__icontains=q))

    p = Paginator(authors, objects_per_page)
    page_obj = p.get_page(page_number)
    return render(
        request,
        "library/authors_list.html",
        {"page_obj": page_obj, "per_page": objects_per_page}
    )

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
