from django.shortcuts import render
from blog.models import Post
from blog.forms import PostForm
# Create your views here.

def posts_list(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

    form = PostForm()
    posts = Post.objects.all()

    return render(request, "blog/posts_list.html", {"posts": posts, "form": form})