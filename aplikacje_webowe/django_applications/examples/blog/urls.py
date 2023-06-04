from django.urls import path
from blog.views import posts_list

app_name = 'blog'
urlpatterns = [
    path('', posts_list, name='list'),
]