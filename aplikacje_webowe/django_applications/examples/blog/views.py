from django.shortcuts import render
from django.views.generic import View
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


def post_details(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.user != post.author:
        for field in form.fields:
            form.fields[field].widget.attrs["disabled"] = True


    if request.method == "POST":
        form = PostForm(request.POST, instance=post)


        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    return render(request, "blog/post_details.html", {"post": post, "form": form})



class PostCreateListeView(View):
    template_name = "blog/posts_list.html"
    form_class = PostForm
    model = Post

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"posts": self.model.objects.all(), "form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        return render(request, self.template_name, {"posts": self.model.objects.all(), "form": self.form_class()})