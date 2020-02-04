from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Daftar, DataTK
from .form import DaftarForm, DataTkForm
import sqlite3, collections, json
from .crawler1 import crawler
import requests

# import json, requests, urllib

def index(request):

    datas = Daftar.objects.all()
    # datas = DataTK.objects.all()
    # print(datas)
    return render(request, 'daftar/winback_list.html', {'datas': datas})

# def toJson():
#     conn = sqlite3.connect("./db.sqlite3")
#     curr = conn.cursor()

#     curr.execute('''
#                     SELECT * FROM  daftar_datatk
#                     ''')
#     rows = curr.fetchall()
#     lists = []
#     for row in rows:
#         d = collections.OrderedDict()
#         d['id'] = row.id
#         d['nik'] = row.nik
#         d['nama'] = row.nama
#         d['tgl_lhr'] = row.tgl_lhr
#         d['tempat_lhr'] = row.tempat_lhr
#         d['alamat'] = row.alamat
#         lists.append(d)
    
#     j = json.dumps(lists)
#     jsfile = 'tenaga_kerja.js'
#     f = open(jsfile, 'w')

#     return f,j

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
    
def daftar_tk(request):
    match = DataTK.objects.all()
    if request.method == "POST":
        form = DaftarForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # karyawan_created.delay(post.id)
            # karyawan_jatuh_tempo.apply_async((post.id,),
            #                                  countdown=60)
            return redirect('daftar:winback')
    else:
        form = DaftarForm()
    return render(request, 'daftar/winback_new.html', {'form': form, 'match':match})

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