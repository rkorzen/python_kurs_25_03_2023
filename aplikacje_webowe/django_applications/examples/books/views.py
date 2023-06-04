from django.shortcuts import render
from books.models import Book
# Create your views here.
from .forms import BookForm, BookForm2, MyForm, MyFormSet

def books_list(request):
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "books/details.html", {"book": book})


def form_view(request):
    formset = MyFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)

    return render(request, 'my_template.html', {'formset': formset})
