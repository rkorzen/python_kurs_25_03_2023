from django.urls import path
from django.views.generic import TemplateView
from .views import books_list, book_details, form_view, HomeTemplateView, BookListView, BookCreateView, BookDetailView

app_name = "books" # przestrzeń nazw aplikacji
urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("books/", BookListView.as_view(), name="list"),
    path("books/create", BookCreateView.as_view(), name="create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="details"),
    path("formview/", form_view, name="formview")

]
