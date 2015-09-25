# coding=utf-8
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from .models import Service, Fonction, Personnel
from .serializers import ServiceSerizalizer, FonctionSerizalizer, PersonnelSerizalizer
__author__ = 'paulguichon'


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerizalizer
    permission_classes = [permissions.AllowAny]


class FonctionViewSet(viewsets.ModelViewSet):
    queryset = Fonction.objects.all()
    serializer_class = FonctionSerizalizer
    permission_classes = [permissions.AllowAny]


class PersonnelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Personnel.objects.all().prefetch_related('fonction')
    serializer_class = PersonnelSerizalizer
    filter_fields = ('service', )

