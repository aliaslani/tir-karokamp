from django.shortcuts import render, get_object_or_404, redirect

from core.models import Post
# Create your views here.


def home(request):
    posts = Post.objects.filter(archived=False)
    data = {"posts": posts}
    return render(request, "core/index.html", context=data)


def post_detail(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    context = {"post": p}
    return render(request, "core/post_detail.html", context=context)


def post_delete(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    p.archived = True
    p.save()
    return redirect("home")
