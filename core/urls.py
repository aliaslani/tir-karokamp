from django.urls import path
from core.views import home, post_detail

urlpatterns = [
    path("", home, name="home"),
    path("post/<post_id>/", post_detail, name="post_detail"),
]
