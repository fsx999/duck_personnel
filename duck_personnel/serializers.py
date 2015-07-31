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
    can_edit = serializers.SerializerMethodField('is_edit')

    def is_edit(self, personne):
        if self.context['request'].user.is_authenticated() and self.context['request'].user.is_superuser:
            return True
        return False

    class Meta:
        model = Personnel
        fields = ('service',
                  'can_edit',
                  'id',
                  'nom',
                  'prenom',
                  'email',
                  'phone',
                  'bureau',
                  'fonction_name_list'
                  )
