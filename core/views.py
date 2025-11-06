from django.shortcuts import render, HttpResponse
from core.models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    data = {"posts": posts}
    return render(request, "core/index.html", context=data)


def post_detail(request, post_id):
    p = Post.objects.filter(id=post_id).first()
    context = {"post": p}

    return render(request, "core/post_detail.html", context=context)
