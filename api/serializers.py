from rest_framework import serializers

from daftar.models import DataTK, Daftar

class DataTkSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataTK
        fields = ('nik', 'nama', 'tempat_lhr',
                    'tgl_lhr', 'alamat')