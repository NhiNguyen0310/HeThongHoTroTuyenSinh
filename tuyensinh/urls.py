
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework .routers import DefaultRouter

r = DefaultRouter()
r.register('categories', views.CategoryViewSet)
r.register('thongtintuyensinhs', views.ThongTinTuyenSinhViewSet)
r.register('loaithongtintuyensinhs', views.LoaiThongTinTuyenSinhViewSet)
r.register('users', views.UserViewSet, basename='user')
r.register('login', views.LoginUser, basename='login')
r.register('bannerschool', views.BannerSchool, basename='bannerschool')
r.register('commentoninforschool', views.CommentOnInforSchool, basename='commentOninforschool')
r.register('standardpointoffaculty', views.StandardPointOfFaculty, basename='standardpointoffaculty')
r.register('facultyofschool', views.FacultyOfSchool, basename='facultyofschool')
urlpatterns = [
    path('api/', include(r.urls))
]