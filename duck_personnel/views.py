# coding=utf-8
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Service, Fonction, Personnel
from .serializers import ServiceSerizalizer, FonctionSerizalizer, PersonnelSerizalizer
__author__ = 'paulguichon'


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerizalizer


class FonctionViewSet(viewsets.ModelViewSet):
    queryset = Fonction.objects.all()
    serializer_class = FonctionSerizalizer


class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerizalizer