from django.urls import path
from .views import hello_view

urlpatterns = [
    path("", hello_view ),  # /
    path("hello/", hello_view ), # /hello
    path("hello/<greetings>/<name>/", hello_view ), # /hello/cos/cos
]
