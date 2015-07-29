# coding=utf-8
from __future__ import unicode_literals
__author__ = 'paulguichon'
from rest_framework import serializers
from .models import Service, Fonction, Personnel


class ServiceSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Service


class FonctionSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Fonction


class PersonnelSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
