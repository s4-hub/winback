from django import forms
from .models import Daftar, DataTK
from django.db.models import Q

class DataTkForm(forms.ModelForm):
    class Meta:
        model = DataTK
        fields = [
            'nik', 'nama', 'tempat_lhr',
            'tgl_lhr', 'alamat'
        ]

# class PkForm(forms.ModelForm):
#     class Meta:
#         model = Pekerjaan
#         fields = ['pekerjaan1', 'pekerjaan2'
#         'lokasi']

#         widgets = {
#                 'pekerjaan1': forms.TextInput(
#                     attrs={'class': 'form-control',
#                 'placeholder': 'Pekerjaan I'}),
#                 'pekerjaan2': forms.TextInput(
#                     attrs={'class': 'form-control'}),
#                 'lokasi': forms.TextInput(
#                     attrs={'class': 'form-control',
#                 }),    

#         }

class DaftarForm(forms.ModelForm):
    class Meta:
        model = Daftar
        
        # exclude = ('DataTk')
        fields = [
                'mail', 'pekerjaan1',
                'pekerjaan2', 'lokasi',
                'no_hp', 'penghasilan',
                'program', 'bulan', 'user_id'
            ]
        
        widgets = {
            # 'nik': forms.TextInput(
            #     attrs={'class': 'form-control',
            #     'value': }),
            'mail': forms.TextInput(
                attrs={'class': 'form-control',
                'type': 'email',
                'placeholder': 'Email'}),
            'pekerjaan1': forms.Select(
                attrs={'class': 'form-control',
            'placeholder': 'Pekerjaan I',
            }),
            'pekerjaan2': forms.Select(
                attrs={'class': 'form-control'}),
            'lokasi': forms.Select(
                attrs={'class': 'form-control',
            }),
            'no_hp': forms.TextInput(
                attrs={'class': 'form-control',
                'placholder': 'NO Hp'}),
            'penghasilan': forms.TextInput(
                attrs={'class': 'form-control'}),
            'program': forms.Select(
                attrs={'class': 'form-control'}),
            'bulan': forms.Select(
                attrs={'class': 'form-control'}),
            
        }    