
from django.contrib import admin
from django.urls import path, include
from . import  views
from rest_framework .routers import DefaultRouter

r = DefaultRouter()
r.register('categories', views.CategoryViewSet)
r.register('thongtintuyensinhs', views.ThongTinTuyenSinhViewSet)
r.register('loaithongtintuyensinhs', views.LoaiThongTinTuyenSinhViewSet)
r.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(r.urls)),
]