from django.urls import path
from . import views

app_name = 'daftar'
urlpatterns = [
    path('', views.index, name='daftar'),
    # path('karyawan/<int:pk>/delete', views.karyawan_delete, name='karyawan_delete'),
    # path('karyawan/<int:pk>/edit', views.karyawan_edit, name='karyawan_edit'),
    # path('karyawan/<int:pk>/', views.karyawan_detail, name='karyawan_detail'),
    path('cari/', views.cari, name='cari'),
    path('add/', views.daftar_tk, name='add_tk'),
    # path('daftar/', views.karyawan_list, name='karyawan_list'),
    #path('pk_list', views.pk_list, name='pk_list'),
   


]