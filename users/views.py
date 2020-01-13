from django.shortcuts import render, redirect
from .form import UsersForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Selamat Datang {username}!')
        return redirect('home')
    else:
        form = UsersForm()
    return render(request, 'users/register.html', {'form': form})