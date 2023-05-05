import hashlib

from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import Response
from rest_framework import viewsets, generics, parsers, permissions
from .models import ThongTinTuyenSinh, Category, LoaiThongTinTuyenSinh, User, BannerSchool, InforSchool, \
    CommentOnInforSchool, FacultyOfSchool, FacultyManagerOfSchool, StandardPointOfFaculty
from .serializers import ThongTinTuyenSinhSerializer, CategorySerializer, LoaiThongTinTuyenSinhSerializer, \
    UserSerializer, BannerSchoolSerializer, InforSchoolSerializer, CommentOnInforSchoolSerializer, \
    FacultyOfSchoolSerializer, FacultyManagerOfSchoolSerializer, StandardPointOfFacultySerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .token import get_tokens_for_user


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
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class LoginUser(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        # check user
        data = request.data
        user_name = data['username']
        password = hashlib.md5(data['password'].encode('utf-8')).hexdigest()
        user = User.objects.get(username=user_name, password=password)

        if not user:
            return Response(data="error", status=400)

        # create user format dict
        serializer = UserSerializer(user)

        # create token for user
        token = get_tokens_for_user(user=User(**serializer.data))

        return Response(data={
            "messenger": "Successfully",
            "access_token": "Bearer" + token['access'],
            "refresh_token": token['refresh']
        }, status=200)


class BannerSchool(viewsets.ModelViewSet):
    queryset = BannerSchool.objects.all()
    serializer_class = BannerSchoolSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class InforSchool(viewsets.ModelViewSet):
    queryset = InforSchool.objects.all()
    serializer_class = InforSchoolSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CommentOnInforSchool(viewsets.ModelViewSet):
    queryset = CommentOnInforSchool.objects.all()
    serializer_class = CommentOnInforSchoolSerializer
    permission_classes = [permissions.IsAuthenticated]


class StandardPointOfFaculty(viewsets.ModelViewSet):
    queryset = StandardPointOfFaculty.objects.all()
    serializer_class = StandardPointOfFacultySerializer
    permission_classes = [permissions.IsAuthenticated]


class FacultyManagerOfSchool(viewsets.ModelViewSet):
    queryset = FacultyManagerOfSchool.objects.all()
    serializer_class = FacultyManagerOfSchoolSerializer
    permission_classes = [permissions.IsAuthenticated]


class FacultyOfSchool(viewsets.ModelViewSet):
    queryset = FacultyOfSchool.objects.all()
    serializer_class = FacultyOfSchoolSerializer
    permission_classes = [permissions.IsAuthenticated]
