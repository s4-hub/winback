from django.contrib import admin
from . models import Daftar
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['user_id', 'nama', 'passwd', 'role']
#     list_filter = ['user_id', 'nama']

@admin.register(Daftar)
class DaftarAdmin(admin.ModelAdmin):
    list_display = [
        'nik', 'nama', 'no_hp', 'pekerjaan',
        'lokasi', 'program', 'bulan', 'total'
    ]