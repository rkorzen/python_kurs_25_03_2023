from django.urls import path
from blog.views import posts_list, post_details

app_name = 'blog'
urlpatterns = [
    path('', posts_list, name='list'),
    path("<int:id>/", post_details, name="details"),
]