from django.urls import path
from .views import simple_plot, simple_import, simple_import_details

app_name = "plots"
urlpatterns = [
    path("simpleplot/", simple_plot, name="simpleplot"),
    path("simpleimport/", simple_import, name="simpleimport"),
    path("simpleimport/<import_date>", simple_import_details, name="simpleimport_details"),
]
