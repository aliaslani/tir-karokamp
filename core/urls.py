from django.urls import path
from core.views import home, post_detail, post_delete, create_post, edit_post, add_score

urlpatterns = [
    path("", home, name="home"),
    path("post/<post_id>/", post_detail, name="post_detail"),
    path("post/delete/<int:post_id>/", post_delete, name="post_delete"),
    path("new/post/", create_post, name="create_post"),
    path("post/<post_id>/edit/", edit_post, name="edit_post"),
    path("post/score/add/<int:post_id>/", add_score, name="post_score"),
]
