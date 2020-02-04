from django.contrib import admin
from . models import Daftar, DataTK
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['user_id', 'nama', 'passwd', 'role']
#     list_filter = ['user_id', 'nama']

@admin.register(DataTK)
class DataTKAdmin(admin.ModelAdmin):
    list_display = [
        'nik', 'nama', 'tempat_lhr', 'tgl_lhr', 'alamat'
    ]

@admin.register(Daftar)
class DaftarAdmin(admin.ModelAdmin):
    list_display = [
        'mail', 'no_hp', 'penghasilan',
        'program', 'bulan', 'user_id', 'total'
    ]