from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post
from django.contrib import messages
from core.forms import PostForm
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


# def create_post(request):
#     form = PostForm()
#     if request.method == "POST":
#         title = request.POST.get("title")
#         title = request.GET.get("title")
#         content = request.POST.get("content")
#         username = request.POST.get("username")
#         published_at = request.POST.get("published_at")
#         published = request.POST.get("published")
#         if published == "yes":
#             published = True
#         else:
#             published = False
#         user = MyUser.objects.filter(username=username).first()
#         new_post = Post.objects.create(
#             title=title,
#             content=content,
#             user=user,
#             published=published,
#             published_at=published_at,
#         )
#         print(new_post)
#         return redirect("home")


#     return render(request, "core/create_post.html", {"form": form})
def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            title = data.get("title")
            content = data.get("content")
            user = data.get("user")
            published_at_date = data.get("published_at_date")
            published_at_time = data.get("published_at_time")
            published = data.get("published")
            new_post = Post.objects.create(
                title=title,
                content=content,
                user=user,
                published_at=f"{published_at_date} {published_at_time}",
                published=published,
            )
            if len(content) > 15:
                messages.success(request, "پست شما با موفقیت ثبت شد")
            else:
                messages.warning(request, "پست شما با موفقیت ثبت شد اما")
            return redirect("home")

    return render(request, "core/create_post.html", {"form": form})
