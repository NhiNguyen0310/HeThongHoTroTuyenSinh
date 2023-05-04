from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework import viewsets, generics, parsers, permissions
from .models import ThongTinTuyenSinh, Category, LoaiThongTinTuyenSinh, User
from .serializers import ThongTinTuyenSinhSerializer, CategorySerializer, LoaiThongTinTuyenSinhSerializer, UserSerializer

# Create your views here.

def index(request):
    return HttpResponse("Trang Chủ")

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LoaiThongTinTuyenSinhViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = LoaiThongTinTuyenSinh.objects.all()
    serializer_class = LoaiThongTinTuyenSinhSerializer

class ThongTinTuyenSinhViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ThongTinTuyenSinh.objects.filter(active=True)
    serializer_class = ThongTinTuyenSinhSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        # u = request.user
        # if request.method.__eq__('PUT'):
        #     for k, v in request.data.items():
        #         if k.__eq__('password'):
        #             u.set_password(k)
        #         else:
        #             setattr(u, k, v)
        #     u.save()

        return Response(UserSerializer(request.user))

