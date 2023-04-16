from django.urls import path
from .views import calculator

urlpatterns = [
    # /maths/add/1/2/
    path("maths/<op>/<int:a>/<int:b>/", calculator),

    # /maths/add/aa/bb
]
