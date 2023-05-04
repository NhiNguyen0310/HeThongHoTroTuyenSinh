from rest_framework import serializers
from .models import ThongTinTuyenSinh, Category, LoaiThongTinTuyenSinh, User

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
        fields = ['id', 'title','image','created_date','category','loaithongtintuyensinh']


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='avatar')

    def get_image(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % obj.avatar.name) if request else ''

    def create(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.set_password(u.password)
        u.save()
        return u

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'avatar', 'image']
        extra_kwargs = {
            'avatar': {'write_only': 'True'},
            'password': {'write_only': 'True'}
        }

