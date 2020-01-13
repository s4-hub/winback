from django.shortcuts import render, redirect
from .form import UsersForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@csrf_protect
def register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # last_name = form.cleaned_data.get('last_name')
            # messages.success(request, f'Selamat Datang {first_name} {last_name}!')
            messages.success(request, f'Akun {username} berhasil dibuat')
        return redirect('login')
    else:
        form = UsersForm()
    return render(request, 'users/register.html', {'form': form})


def masuk(request):
    if request.method == "POST":
        
        uname = request.POST['username']
        pwd = request.POST['password']
        # print(uname)
        # print(pwd)
        user = authenticate(request, username=uname, password=pwd)
        print(user)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     return redirect('register')
    return render(request, 'users/login.html')