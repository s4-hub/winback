# Generated by Django 3.0 on 2020-01-12 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Daftar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16)),
                ('nama', models.CharField(max_length=50)),
                ('tempat_lhr', models.CharField(max_length=30)),
                ('tgl_lhr', models.DateField()),
                ('alamat', models.TextField()),
                ('no_hp', models.CharField(max_length=15)),
                ('pekerjaan', models.CharField(max_length=30)),
                ('lokasi', models.CharField(max_length=30)),
                ('penghasilan', models.DecimalField(decimal_places=0, max_digits=10)),
                ('program', models.IntegerField(choices=[(1, 'JKK & JKM'), (2, 'JKK, JKM & JHT')])),
                ('bulan', models.IntegerField(choices=[(1, '1 Bulan'), (3, '3 Bulan'), (6, '6 Bulan'), (12, '12 Bulan')])),
                ('tgl_buat', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
