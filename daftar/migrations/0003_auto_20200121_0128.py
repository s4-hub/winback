# Generated by Django 3.0 on 2020-01-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar', '0002_auto_20200121_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftar',
            name='mail',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daftar',
            name='lokasi',
            field=models.CharField(choices=[('1101', 'ACEH SELATAN'), ('1102', 'ACEH TENGGARA'), ('1103', 'ACEH TIMUR'), ('1104', 'ACEH TENGAH'), ('1105', 'ACEH BARAT'), ('1106', 'ACEH BESAR'), ('1107', 'PIDIE'), ('1108', 'ACEH UTARA'), ('1109', 'SIMEULUE'), ('1110', 'ACEH SINGKIL'), ('1111', 'BIREUEN'), ('1112', 'ACEH BARAT DAYA'), ('1113', 'GAYO LUES'), ('1114', 'ACEH JAYA'), ('1115', 'NAGAN RAYA'), ('1116', 'ACEH TAMIANG'), ('1117', 'BENER MERIAH'), ('1118', 'PIDIE JAYA'), ('1171', 'KOTA BANDA ACEH'), ('1172', 'KOTA SABANG'), ('1173', 'KOTA LHOKSEUMAWE'), ('1174', 'KOTA LANGSA'), ('1175', 'KOTA SUBULUSSALAM')], max_length=30),
        ),
        migrations.AlterField(
            model_name='daftar',
            name='program',
            field=models.CharField(choices=[('T', 'JKK & JKM'), ('L', 'JKK, JKM & JHT')], max_length=12),
        ),
    ]