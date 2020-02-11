from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms.formsets import formset_factory
from .models import Daftar, DataTK
from .form import DaftarForm, DataTkForm
import sqlite3, collections, json
from .crawler1 import crawler
import requests

# import json, requests, urllib

def index(request):

    datas = Daftar.objects.select_related('nik')
    # daftar = Daftar.objects.all()
    # data = DataTK.objects.all()
    # datas = DataTK.objects.all()
    # print(datas)
    return render(request, 'daftar/winback_list.html', {'datas':datas})

def cari(request):
   
    if request.method == 'POST':
        nik = request.POST['ktp']
        
        if not nik:
            messages.error(request, 'NIK tidak boleh kosong')
            return render(request, 'daftar/cari.html')
        else:
            crawler(nik)
            if nik:
                
                match = DataTK.objects.filter(Q(nik__icontains=nik))
            
                
                if match:
                    
                    return render(request, 'daftar/cari.html', {'match': match})
                    # return redirect('add/')
                else:
                    messages.error(request, 'NIK tidak ditemukan')
            else:
                
                return HttpResponse('Sukses')
        
    return render(request, 'daftar/cari.html') 
    
def daftar_tk(request, pk):

    data_master = get_object_or_404(DataTK, pk=pk)
    # DataTKFormSet = formset_factory(DataTK)
    if request.method == "POST":
        form = DaftarForm(request.POST, instance=data_master)
        # formset = DataTKFormSet(request.POST)
        if form.is_valid():
            # , formset.is_valid()]):
            post = form.save(commit=False)
            post.user_id = request.user
            post = form.save()
            # post.save()
            # for set_form in formset:
            #     if set_form.cleaned_data:
            #         reg = set_form.save(commit=False)
            #         reg.user_id = request.user
            #         reg.nik = post
            #         reg.save()
            # nik = form.cleaned_data.get('nik')
            # karyawan_created.delay(post.id)
            # karyawan_jatuh_tempo.apply_async((post.id,),
            #                                  countdown=60)
            return redirect('daftar:home', pk=data_master)
    else:
        form = DaftarForm(instance=data_master)
        # formset = DataTKFormSet()

    return render(request, 'daftar/winback_new.html', {'form': form})

# def getJson(request):
#     response = requests.get('http://localhost:8000/api/data_tk/')
#     data = response.json()
#     return render(request, 'daftar/winback_new.html', {
#         'nik':data['nik'],
#         'nama':data['nama'],
#         'tempat':data['tempat_lhr'],
#         'tgl_lhr':data['tgl_lhr'],
#         'alamat':data['alamat']
#     })