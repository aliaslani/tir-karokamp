from tkinter import N
from django.db import models
from accounts.models import MyUser


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField()
    rate = models.PositiveSmallIntegerField(default=0)
    archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"

    def __str__(self):
        return f"{self.title}"


class Score(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    rate = models.PositiveSmallIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="rates")

    def __str__(self):
        return str(self.rate)
