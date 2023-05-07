from django.shortcuts import render

from posts.models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/post_details.html", {"post": post})
