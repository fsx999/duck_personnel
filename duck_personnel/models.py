# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
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
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField("Téléphone", null=True, max_length=10)
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.nom, self.prenom, self.fonction)

    def save(self, *args, **kwargs):
        if not self.email and self.user and self.user.email:
            self.email = self.user.email
        super(Personnel, self).save(*args, **kwargs)
