from django.shortcuts import render
from accounts.models import MyUser


def profile_view(request):
    return render(request, "accounts/profile.html")
