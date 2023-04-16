from django.urls import path
from .views import calculator, kalkulator_v2

urlpatterns = [
    # /maths/add/1/2/
    path("maths/<op>/<int:a>/<int:b>/", calculator),
    path("maths/", kalkulator_v2)
    # /maths/add/aa/bb
]
