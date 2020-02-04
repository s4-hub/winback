from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import decimal, requests, sqlite3
from bs4 import BeautifulSoup
import json
# import crawler1
# Create your models here.


PEKERJAAN = [
('P001','PETANI/PEKEBUN'),
('P002','PETERNAK'),
('P003','NELAYAN/PERIKANAN'),
('P004','TRANSPORTASI'),
('P005','BURUH HARIAN LEPAS'),
('P006','BURUH TANI/PERKEBUNAN'),
('P007','BURUH NELAYAN/PERIKANAN'),
('P008','BURUH PETERNAKAN'),
('P009','PEMBANTU RUMAH TANGGA'),
('P010','TUKANG CUKUR'),
('P011','TUKANG LISTRIK'),
('P012','TUKANG BATU'),
('P013','TUKANG KAYU'),
('P014','TUKANG SOL SEPATU'),
('P015','TUKANG LAS/PANDAI BESI'),
('P016','TUKANG JAHIT'),
('P017','TUKANG GIGI'),
('P018','PENATA RIAS'),
('P019','PENATA BUSANA'),
('P020','PENATA RAMBUT'),
('P021','MEKANIK'),
('P022','SENIMAN'),
('P023','TABIB'),
('P024','PARAJI'),
('P025','PERANCANG BUSANA'),
('P026','PENTERJEMAH'),
('P027','IMAM MESJID'),
('P028','PENDETA'),
('P029','PASTOR'),
('P030','WARTAWAN'),
('P031','USTADZ/MUBALIGH'),
('P032','JURU MASAK'),
('P033','PROMOTOR ACARA'),
('P034','DOSEN'),
('P035','GURU'),
('P036','PENGACARA'),
('P037','NOTARIS'),
('P038','ARSITEK'),
('P039','KONSULTAN'),
('P040','DOKTER'),
('P041','BIDAN'),
('P042','APOTEKER'),
('P043','PSIKIATER/PSIKOLOG'),
('P044','PENYIAR RADIO'),
('P045','PELAUT'),
('P046','PENELITI'),
('P047','SOPIR'),
('P048','PIALANG'),
('P049','PARANORMAL'),
('P050','PEDAGANG'),
('P051','BIARAWATI'),
('P052','WIRASWASTA'),
('P053','MITRA GOJEK'),
('P054','MITRA GRAB'),
('P055','MITRA UBER'),
('P056','PEKERJA MAGANG'),
('P057','SISWA KERJA PRAKTEK'),
('P058','TENAGA HONORER (SELAIN PENYELENGGARA NEGARA)'),
('P059','NARAPIDANA DALAM PROSES ASIMILASI'),
('P060','ATLET'),
('P061','ARTIS'),
('P062','JURU PARKIR'),
('P063','TUKANG PIJAT'),
('P064','PEMANDU LAGU'),
('P065','PENDAMPING DESA'),
('P066','BURUH BONGKAR MUAT/BAGASI'),
('P067','RELAWAN TAGANA/RELAWAN BENCANA'),
('P068','TUKANG SAMPAH'),
('P069','PEMULUNG'),
('P070','MARBOT MESJID'),
('P071','MITRA GOJEK-GO LIFE'),

    
    
]

PROGRAM = [
    ('T', 'JKK & JKM'),
    ('L', 'JKK, JKM & JHT'),
]

BULAN = [
    (1, '1 Bulan'),
    (3, '3 Bulan'),
    (6, '6 Bulan'),
    (12, '12 Bulan')
]

LOKASI = [
    ('1101','ACEH SELATAN'),
    ('1102','ACEH TENGGARA'),
    ('1103','ACEH TIMUR'),
    ('1104','ACEH TENGAH'),
    ('1105','ACEH BARAT'),
    ('1106','ACEH BESAR'),
    ('1107','PIDIE'),
    ('1108','ACEH UTARA'),
    ('1109','SIMEULUE'),
    ('1110','ACEH SINGKIL'),
    ('1111','BIREUEN'),
    ('1112','ACEH BARAT DAYA'),
    ('1113','GAYO LUES'),
    ('1114','ACEH JAYA'),
    ('1115','NAGAN RAYA'),
    ('1116','ACEH TAMIANG'),
    ('1117','BENER MERIAH'),
    ('1118','PIDIE JAYA'),
    ('1171','KOTA BANDA ACEH'),
    ('1172','KOTA SABANG'),
    ('1173','KOTA LHOKSEUMAWE'),
    ('1174','KOTA LANGSA'),
    ('1175','KOTA SUBULUSSALAM'),

]

# class User(models.Model):
#     user_id = models.CharField(max_length=8)
#     passwd = models.CharField(max_length=16)
#     role = models.IntegerField(choices=ROLE)
#     nama = models.CharField(max_length=50)

class DataTK(models.Model):
    nik = models.CharField(max_length=16, blank=False)
    nama = models.CharField(max_length=50)
    tempat_lhr = models.CharField(max_length=30)
    tgl_lhr = models.CharField(max_length=10)
    alamat = models.TextField()
    
    # def getjson(self):
    #     r = crawler1(y)
   

class Daftar(models.Model):
    nik = models.ForeignKey(DataTK, on_delete=models.CASCADE)   
    mail = models.EmailField()    
    no_hp = models.CharField(max_length=15)
    pekerjaan1 = models.CharField(choices=PEKERJAAN, max_length=50)
    pekerjaan2 = models.CharField(choices=PEKERJAAN, max_length=50, blank=True)
    lokasi = models.CharField(choices=LOKASI, max_length=30)
    penghasilan = models.FloatField()
    program = models.CharField(choices=PROGRAM, max_length=12)
    bulan = models.IntegerField(choices=BULAN)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tgl_buat = models.DateTimeField(auto_now_add=True)
    # total = models.DecimalField(max_digits=10, decimal_places=2)
    def total(self):

        if (self.program == 1):
            jkk = decimal.Decimal(self.penghasilan) * decimal.Decimal('0.01')
            jkm = 6800
            bln = self.bulan
            self.total = bln * (jkk + jkm)
            # return self.total
        else:
            jkk = decimal.Decimal(self.penghasilan) * decimal.Decimal('0.01')
            jht = decimal.Decimal(self.penghasilan) * decimal.Decimal('0.02')
            jkm = 6800
            bln = self.bulan
            self.total = self.bulan * (jkk + jht + jkm)
        return self.total
