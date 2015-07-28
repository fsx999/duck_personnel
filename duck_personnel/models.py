# coding=utf-8
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible

__author__ = 'paulguichon'
from django.db import models
from treebeard.mp_tree import MP_Node


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
class Personnel(MP_Node):
    nom = models.CharField('Nom', max_length=30)
    prenom = models.CharField('Prénom', max_length=30)
    fonction = models.ForeignKey(Fonction)

    def __str__(self):
        return "{} {} {}".format(self.nom, self.prenom, self.fonction)