from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, MyUser

# Create your views here.
from core.forms import PostForm


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


def create_post(request):
    form = PostForm()
    if request.method == "POST":
        title = request.POST.get("title")
        title = request.GET.get("title")
        content = request.POST.get("content")
        username = request.POST.get("username")
        published_at = request.POST.get("published_at")
        published = request.POST.get("published")
        if published == "yes":
            published = True
        else:
            published = False
        user = MyUser.objects.filter(username=username).first()
        new_post = Post.objects.create(
            title=title,
            content=content,
            user=user,
            published=published,
            published_at=published_at,
        )
        print(new_post)
        return redirect("home")

    return render(request, "core/create_post.html", {"form": form})
