from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework import viewsets, generics, parsers, permissions
from .models import ThongTinTuyenSinh, Category, LoaiThongTinTuyenSinh, User
from .serializers import ThongTinTuyenSinhSerializer, CategorySerializer, LoaiThongTinTuyenSinhSerializer, \
    UserSerializer


# Create your views here.

def index(request):
    return HttpResponse("Trang Chủ")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LoaiThongTinTuyenSinhViewSet(viewsets.ModelViewSet):
    queryset = LoaiThongTinTuyenSinh.objects.all()
    serializer_class = LoaiThongTinTuyenSinhSerializer


class ThongTinTuyenSinhViewSet(viewsets.ModelViewSet):
    queryset = ThongTinTuyenSinh.objects.filter(active=True)
    serializer_class = ThongTinTuyenSinhSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


