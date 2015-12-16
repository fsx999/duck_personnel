# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import Group


@python_2_unicode_compatible
class Service(MPTTModel):
    label = models.CharField('Service', max_length=120)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Fonction(models.Model):
    label = models.CharField('Fonction', max_length=120)
    code = models.CharField('Code Employee', max_length=1, choices=(('R', 'Responsable'),
                                                                    ('E', 'Normale')))

    groups_permissions = models.ManyToManyField(Group)

    def __str__(self):
        return "{}".format(self.label)


@python_2_unicode_compatible
class Personnel(MPTTModel):
    nom = models.CharField('Nom', max_length=30)
    prenom = models.CharField('Prénom', max_length=30)
    fonction = models.ManyToManyField(Fonction, null=True)
    service = models.ForeignKey(Service, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField("Téléphone", null=True, max_length=10, blank=True)
    bureau = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)


    @property
    def fonction_name_list(self):
        return [x.label for x in self.fonction.all()]
        # return self.fonction.values_list('label', flat=True)

    @property
    def get_fields_list(self):
        fonctions = ', '.join(self.fonction_name_list)
        return [
                self.nom,
                self.prenom,
                self.service.label,
                self.email,
                self.phone,
                self.bureau,
                fonctions,
        ]

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

    def save(self, *args, **kwargs):
        if not self.email and self.user and self.user.email:
            self.email = self.user.email
        super(Personnel, self).save(*args, **kwargs)

