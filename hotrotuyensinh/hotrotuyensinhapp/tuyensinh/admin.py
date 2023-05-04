from django.contrib import admin
from .models import Category, LoaiThongTinTuyenSinh, ThongTinTuyenSinh
# Register your models here.
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ThongTinTuyenSinhForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = ThongTinTuyenSinh
        fields = '__all__'

class ThongTinTuyenSinhAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'active']
    search_fields = ['title']
    list_filter = ['id', 'title', 'created_date']
    form = ThongTinTuyenSinhForm



admin.site.register(Category)
admin.site.register(LoaiThongTinTuyenSinh)
admin.site.register(ThongTinTuyenSinh, ThongTinTuyenSinhAdmin)