
from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors_list, name="authors_list"),
    path("autorzy/<int:id>/", views.author_details, name="author_details"),
    path("books/", views.books_list, name="books_list"),
    path("books/<int:id>/", views.book_details, name="book_details"),

]