from django.urls import path
from core.views import home, post_detail, post_delete

urlpatterns = [
    path("", home, name="home"),
    path("post/<post_id>/", post_detail, name="post_detail"),
    path("post/delete/<int:post_id>/", post_delete, name="post_delete"),
]
