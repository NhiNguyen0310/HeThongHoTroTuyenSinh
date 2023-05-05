from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m', null=False)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

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
    view_number = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    loaithongtintuyensinh = models.ForeignKey(LoaiThongTinTuyenSinh, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='thongtintuyensinhs/%Y/%m', null=True)

    def __str__(self):
        return self.title


class BannerSchool(BaseModel):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    img_banner = models.ImageField(upload_to="banner/%y%m%d", blank=True, null=True)


class CommentOnInforSchool(BaseModel):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=1000, null=False)


class InforSchool(BaseModel):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=10000, null=False)
    img = models.ImageField(upload_to="infoschoo/%y%m%d", null=True)


class StandardPointOfFaculty(BaseModel):
    content = models.CharField(max_length=1000, null=False)
    name_faculty = models.CharField(max_length=100, null=True)


class FacultyManagerOfSchool(BaseModel):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=10000, null=False)
    website = models.CharField(max_length=100, null=False)
    video = models.CharField(max_length=100, null=True)
    standard_point = models.ForeignKey(StandardPointOfFaculty, on_delete=models.CASCADE, null=True)


class FacultyOfSchool(BaseModel):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100, blank=True, null=False)
    infor_faculty = models.ForeignKey(FacultyManagerOfSchool, on_delete=models.CASCADE, null=True)
    operation_day = models.DateTimeField(default=datetime.now())
