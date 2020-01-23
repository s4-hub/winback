from django.shortcuts import render, redirect
from .form import UsersForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout_then_login
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

@csrf_protect
def masuk(request, next=None):
    if request.method == "POST":
        form = UsersForm(request.POST)    

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)
            
            messages.success(request, f'Selamat Datang {username}')               
            return redirect('home')
        else:
            messages.error(request, f'Akun atau password anda Salah')
            return redirect('login')   
    else:
        form = UsersForm()
           
    return render(request, 'users/login.html', {'form': form})


def singout(request):
    # if request.method == "POST":
        
    #     username = request.POST['username']     
            
    logout(request)
    messages.add_message(request, messages.INFO,'Akun berhasil keluar')
    return redirect('login')

