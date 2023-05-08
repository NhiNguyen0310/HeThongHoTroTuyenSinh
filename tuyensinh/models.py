from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=100, null=False)


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
    category = models.ManyToManyField(Category)
    loaithongtintuyensinh = models.ManyToManyField(LoaiThongTinTuyenSinh)
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class BannerSchool(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    img_banner = models.CharField(max_length=100, blank=True, null=True)


class CommentOnInforSchool(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=1000, null=False)
    thongtintuyensinh = models.ForeignKey(ThongTinTuyenSinh, on_delete=models.CASCADE, null=True, blank=True)


class FacultyOfSchool(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_faculty = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=False, default='')
    website = models.CharField(max_length=100, null=False, default='')
    video = models.CharField(max_length=100, null=True, default='')
    operation_day = models.DateTimeField(default=datetime.now())


class StandardPointOfFaculty(BaseModel):
    content = models.CharField(max_length=1000, null=False)
    year = models.CharField(max_length=20, null=False, default='')
    facultyofschool = models.ManyToManyField(FacultyOfSchool)
