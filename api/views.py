from rest_framework import viewsets

from .serializers import DataTkSerializers, DaftarSerializers
from daftar.models import DataTK, Daftar


class DataTkViewSet(viewsets.ModelViewSet):
    queryset = DataTK.objects.all().order_by('nik')
    serializer_class = DataTkSerializers

class DaftarViewSet(viewsets.ModelViewSet):
    queryset = Daftar.objects.all()
    serializer_class = DaftarSerializers