from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Daftar, DataTK
from .form import DaftarForm, DataTkForm

# import json, requests, urllib

def index(request):

    datas = Daftar.objects.all()
    # print(datas)
    return render(request, 'daftar/winback_list.html', {'datas': datas})
    
def daftar_tk(request):
    if request.method == "POST":
        # cform = DaftarForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # karyawan_created.delay(post.id)
            # karyawan_jatuh_tempo.apply_async((post.id,),
            #                                  countdown=60)
            return redirect('daftar:winback')
    else:
        form = DaftarForm()
    return render(request, 'daftar/winback_new.html', {'form': form})


# def daftar_tk(request):
#     url = 'http://smile.bpjsketenagakerjaan.go.id/smile/mod_kn/ajax/kn5000_detail.php?NIK=1103041606770002'
#     r = urllib.request.urlopen(url)
    
#     print(r.json)
#     if request.method == "POST":
#         form = DaftarForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('winback')
#     else:
#         form = DaftarForm()
#     return render(request, 'daftar/winback_list.html', {'datas': datas})