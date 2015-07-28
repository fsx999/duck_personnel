# coding=utf-8
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible

__author__ = 'paulguichon'
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class Service(models.Model):
    label = models.CharField('Pole', max_length=120)

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Fonction(models.Model):
    label = models.CharField('Role', max_length=120)
    service = models.ForeignKey(Service)

    def __str__(self):
        return "{} {}".format(self.label, self.service)


@python_2_unicode_compatible
class Personnel(MPTTModel):
    nom = models.CharField('Nom', max_length=30)
    prenom = models.CharField('Prénom', max_length=30)
    fonction = models.ForeignKey(Fonction)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return "{} {} {}".format(self.nom, self.prenom, self.fonction)