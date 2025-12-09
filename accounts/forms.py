from django import forms
from accounts.models import MyUser
from django.core.validators import FileExtensionValidator


from django.http import JsonResponse
class RegisterForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        validators=[FileExtensionValidator(["jpg", "png"], "فرمت فایل معتبر نیست")]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-contrl"}),
        label="تکرار گذرواژه",
    )

    class Meta:
        model = MyUser
        fields = [
            "username",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "profile_picture",
            "birthdate",
        ]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = MyUser.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError(
                "کاربری با این نام کاربری قبلا ثبت نام کرده است."
            )
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        confirm_password = data.pop("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("گذرواژه با تکرار آن مطابقت ندارد")
        return data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
