from re import A, M
from django import forms
from django.forms import Form

from core.models import MyUser


class PostForm(Form):
    title = forms.CharField(
        max_length=30,
        label="عنوان",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "عنوان"}),
    )
    content = forms.TextInput()
    user = forms.CharField(max_length=20)
    published = forms.BooleanField()
    published_at = forms.DateTimeField()
