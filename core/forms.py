from cProfile import label
from django import forms
from core.models import MyUser, Post


class EditPostForm(forms.ModelForm):
    title = forms.CharField(
        label="عنوان", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "published",
            "archived",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            )
        }


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=9,
        label="عنوان",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "عنوان"}),
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}), label="محتوا"
    )
    user = forms.ModelChoiceField(
        queryset=MyUser.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    published = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="منتشر شود",
        label_suffix="",
    )
    published_at_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={"class": "form-control"})
    )
    published_at_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"class": "form-control", "placeholder": "12:22"})
    )

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise forms.ValidationError("طول محتوا نمی تواند کمتر از ۱۰ کاراکتر باشد")
        return content

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        content = data.get("content")
        if content and title not in content:
            raise forms.ValidationError("حتما باید عنوان در محتوا نیز وجود داشته باشد.")
        return self.cleaned_data
