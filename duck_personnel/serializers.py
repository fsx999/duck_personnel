# coding=utf-8
from __future__ import unicode_literals
__author__ = 'paulguichon'
from rest_framework import serializers
from .models import Service, Fonction, Personnel


class ServiceSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('label', 'id')


class FonctionSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Fonction


class PersonnelSerizalizer(serializers.ModelSerializer):
    fonction__service = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Personnel
        fields = ('fonction__service',
                   'nom' ,
                    'prenom',
                    'email',
                    'phone',
                    'bureau',)
