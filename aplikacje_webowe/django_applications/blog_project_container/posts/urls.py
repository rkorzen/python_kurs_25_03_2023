from django.urls import path

from posts import views

urlpatterns = [
    path("posts", views.post_list, name="post_list"),
    path("posts/<int:id>", views.post_details, name="post_details"),
]