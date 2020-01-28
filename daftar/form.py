from django import forms
from .models import Daftar, DataTK

class DataTkForm(forms.ModelForm):
    class Meta:
        model = DataTK
        fields = [
            'nik', 'nama', 'tempat_lhr',
            'tgl_lhr', 'alamat'
        ]

class DaftarForm(forms.ModelForm):
    class Meta:
        model = Daftar
        # exclude = ('DataTk')
        fields = [
                'mail', 'no_hp', 'pekerjaan1',
                'pekerjaan2', 'lokasi', 'penghasilan',
                'program', 'bulan', 'user_id'
            ]
        
        widgets = {
            'nik': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Nik'}),
            'nama': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Nama',
                }),
            # 'tgl_lhr': forms.TextInput(
            #     attrs={'class': 'form-control',
            #     'placeholder': 'Tanggal Lahir',
            #     'data-date-format': 'dd/mm/yyyy',
            #     'id': 'datepicker'}),
            'tgl_lhr' : forms.TextInput(
                attrs={'class': 'form-control',
                }),
            'tempat_lhr': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Tempat Lahir'}),
            'alamat': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Alamat'
                }),
            'lokasi': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Lokasi'}),
            'penghasilan': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Penghasilan'}),
            'program': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Pilihan Program'}),
            'bulan': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Bulan program'}),    
        }