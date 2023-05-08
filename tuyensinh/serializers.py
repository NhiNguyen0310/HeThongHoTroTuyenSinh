import hashlib

from rest_framework import serializers
from .models import ThongTinTuyenSinh, Category, LoaiThongTinTuyenSinh, User, BannerSchool, \
    CommentOnInforSchool, FacultyOfSchool, StandardPointOfFaculty


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LoaiThongTinTuyenSinhSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoaiThongTinTuyenSinh
        fields = ['id', 'type']


class ThongTinTuyenSinhSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThongTinTuyenSinh
        fields = ['id', 'title', 'image', 'created_date', 'category', 'loaithongtintuyensinh']


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'avatar']
        extra_kwargs = {
            'avatar': {'write_only': 'True'},
            'password': {'write_only': 'True'}
        }

    def create(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.password = hashlib.md5(u.password.encode('utf-8')).hexdigest()
        u.is_staff = True
        u.save()
        return u


class BannerSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerSchool
        fields = ['id', 'user_id', 'img_banner', 'created_date', 'updated_date', 'is_delete']


class CommentOnInforSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOnInforSchool
        fields = ['id', 'user_id', 'content', 'created_date', 'updated_date', 'is_delete', 'thongtintuyensinh']


class FacultyOfSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyOfSchool
        fields = ['id', 'name', 'infor_faculty', 'operation_day', 'is_delete']


class StandardPointOfFacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardPointOfFaculty
        fields = ['id', 'content', 'year', 'facultyofschool']
