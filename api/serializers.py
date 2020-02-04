from rest_framework import serializers

from daftar.models import DataTK, Daftar

class DataTkSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataTK
        fields = ('__all__')

class DaftarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Daftar
        fields = ('__all__')