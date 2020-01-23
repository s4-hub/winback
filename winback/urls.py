from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from daftar import views as daftar_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.masuk, name='login'),
    path('logout/', user_views.singout, name='logout'),
    path('winback/', daftar_views.index, name='winback'),
    path('add/', daftar_views.daftar_tk, name='add'),
    path('', views.index, name='home'),
]
