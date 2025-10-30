from django.db import models

# Create your models here.


class GenderOption(models.TextChoices):
    male = ("m", "مرد")
    female = ("f", "زن")
    none = ("n", "نمی‌خواهم مشخص کنم")


class MyUser(models.Model):
    username = models.CharField(max_length=50, verbose_name="نام کاربری", unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    birthdate = models.DateField("تاریخ تولد")
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GenderOption.choices)

    class Meta:
        verbose_name = "کاربر"


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField()
    rate = models.PositiveSmallIntegerField()
    archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"
