from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import decimal
# Create your models here.

ROLE = [
    (1, 'AR'),
    (2, 'AR Khusus'),
    (3, 'PAP'),
    (4, 'PAP Khusus'),
    
    
]

PROGRAM = [
    (1, 'JKK & JKM'),
    (2, 'JKK, JKM & JHT'),
]

BULAN = [
    (1, '1 Bulan'),
    (3, '3 Bulan'),
    (6, '6 Bulan'),
    (12, '12 Bulan')
]

# class User(models.Model):
#     user_id = models.CharField(max_length=8)
#     passwd = models.CharField(max_length=16)
#     role = models.IntegerField(choices=ROLE)
#     nama = models.CharField(max_length=50)

class Daftar(models.Model):
    nik = models.CharField(max_length=16)
    nama = models.CharField(max_length=50)
    tempat_lhr = models.CharField(max_length=30)
    tgl_lhr = models.DateField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    pekerjaan = models.CharField(max_length=30)
    lokasi = models.CharField(max_length=30)
    penghasilan = models.DecimalField(max_digits=10, decimal_places=0)
    program = models.IntegerField(choices=PROGRAM)
    bulan = models.IntegerField(choices=BULAN)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tgl_buat = models.DateTimeField(auto_now_add=True)
    # total = models.DecimalField(max_digits=10, decimal_places=2)
    def total(self):

        if (self.program == 1):
            jkk = self.penghasilan * decimal.Decimal('0.01')
            jkm = 6800
            bln = self.bulan
            self.total = bln * (jkk + jkm)
            # return self.total
        else:
            jkk = self.penghasilan * decimal.Decimal('0.01')
            jht = self.penghasilan * decimal.Decimal('0.02')
            jkm = 6800
            bln = self.bulan
            self.total = self.bulan * (jkk + jht + jkm)
        return self.total
    