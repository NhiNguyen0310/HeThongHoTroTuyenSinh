from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class LoaiThongTinTuyenSinh(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class ThongTinTuyenSinh(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    content = models.CharField(default="", max_length=10000)
    comment_number = models.IntegerField(default=0)
    view_number = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    loaithongtintuyensinh = models.ForeignKey(LoaiThongTinTuyenSinh, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='thongtintuyensinhs/%Y/%m', null=True)

    def __str__(self):
        return self.title
