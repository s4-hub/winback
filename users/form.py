from django import forms
from django.contrib.auth.models import User

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                'first_name', 'last_name',
                'password'
            ]
        
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'User Name'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Email',
                'type': 'email'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Nama Depan'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Nama Belakang'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Password',
                'type': 'password'}),    
        }