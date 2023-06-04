from django.urls import path
from .views import books_list, book_details, form_view

app_name = "books" # przestrzeń nazw aplikacji
urlpatterns = [
    path("books/", books_list, name="list"),
    path("books/<int:pk>/", book_details, name="details"),
    path("formview/", form_view, name="formview")
]
