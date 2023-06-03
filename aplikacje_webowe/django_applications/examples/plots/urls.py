from django.urls import path
from .views import simple_plot, simple_import

app_name = "plots"
urlpatterns = [
    path("simpleplot/", simple_plot, name="simpleplot"),
    path("simpleimport/", simple_import, name="simpleimport"),
]
