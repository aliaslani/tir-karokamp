from django import forms
from accounts.models import MyUser
from django.core.validators import FileExtensionValidator
from django.contrib.auth.forms import UserCreationForm


from django.http import JsonResponse
class RegisterForm(UserCreationForm):
    profile_picture = forms.ImageField(
        validators=[FileExtensionValidator(["jpg", "png"], "فرمت فایل معتبر نیست")]
    )
    

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "birthdate",
            "profile_picture",
        )
        widgets = {
            "birthdate": forms.DateInput(
                attrs={
                    "type": "text",
                    "id": "birthdate",
                    "class": "form-control",
                }
            ),
        } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Style all fields consistently
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
