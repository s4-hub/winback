# Generated by Django 2.2.7 on 2020-01-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar', '0008_merge_20200129_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatk',
            name='nik',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='datatk',
            name='tgl_lhr',
            field=models.CharField(max_length=10),
        ),
    ]
