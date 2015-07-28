# coding=utf-8
from __future__ import unicode_literals
__author__ = 'paulguichon'
from django.db import models
from treebeard.mp_tree import MP_Node


class Category(models.Model):
    label = models.CharField('Catégorie', max_length=120)


class Personnel(MP_Node):
    last_name = models.CharField('Nom', max_length=30)
    first_name = models.CharField('Prénom', max_length=30)
    category = models.ForeignKey(Category)
