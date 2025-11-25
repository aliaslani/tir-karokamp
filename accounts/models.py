from django.db import models
from django.contrib.auth.models import AbstractUser


class GenderOption(models.TextChoices):
    male = ("m", "مرد")
    female = ("f", "زن")
    none = ("n", "نمی‌خواهم مشخص کنم")


class MyUser(AbstractUser):
    birthdate = models.DateField("تاریخ تولد", null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GenderOption.choices, null=True, blank=True
    )
    profile_picture = models.ImageField(
        "عکس پروفایل",
        upload_to="profile_pictures",
        default="profile_pictures/default.jpg",
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    def __str__(self):
        return f"{self.username}"
