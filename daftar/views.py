from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Daftar
from users.form import UsersForm

def index(request):

    datas = Daftar.objects.all()
    print(datas)
    return render(request, 'daftar/winback_list.html', {'datas': datas})
    