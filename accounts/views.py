from readline import read_init_file
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import MyUser
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout


def profile_view(request):
    return render(request, "accounts/profile.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "ثبت نام شما با موفقیت انجام شد")
            return redirect("login")

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "خوش آمدید")
                return redirect("profile")
            else:
                messages.error(request, 'کاربری با این مشخصات یافت نشد')
                print(username, password, user)
        else:
            print(form.errors)
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید")
    return redirect("login")
