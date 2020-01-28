from rest_framework import viewsets

from .serializers import DataTkSerializers
from daftar.models import DataTK


class DataTkViewSet(viewsets.ModelViewSet):
    queryset = DataTK.objects.all().order_by('nik')
    serializer_class = DataTkSerializers