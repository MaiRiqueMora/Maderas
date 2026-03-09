from django.shortcuts import render
from rest_framework import viewsets
from .models import Camion, Conductor, Cliente, TipoMadera, Carga
from .serializers import CamionSerializer, ConductorSerializer, ClienteSerializer, TipoMaderaSerializer, CargaSerializer


def home(request):
    return render(request, "api/home.html")

def quienes(request):
    return render(request, "api/quienes.html")

def servicios(request):
    return render(request, "api/servicios.html")

def contacto(request):
    return render(request, "api/contacto.html")

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TipoMaderaViewSet(viewsets.ModelViewSet):
    queryset = TipoMadera.objects.all()
    serializer_class = TipoMaderaSerializer

class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
