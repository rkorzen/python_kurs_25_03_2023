from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from books.models import Book
from django.urls import reverse_lazy

# Create your views here.
from .forms import BookForm, BookForm2, MyForm, MyFormSet

class HomeTemplateView(TemplateView):
    template_name = "books/base.html"
def books_list(request):
    books = Book.objects.all()

    if request.method == "POST":
        form = BookForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = BookForm2()

    return render(request, "books/list.html", {"books": books, "form": form})

class BookListView(ListView):
    template_name = "books/list.html"
    model = Book
    context_object_name = "books"


class BookCreateView(CreateView):
    template_name = "books/list.html"
    model = Book
    form_class = BookForm2
    success_url = reverse_lazy("books:list")

class BookDetailView(DetailView):
    template_name = "books/details.html"
    model = Book
    context_object_name = "book"

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
