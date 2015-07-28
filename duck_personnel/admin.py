__author__ = 'paulguichon'
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Personnel, Service, Fonction
import xadmin

class PersonnelAdmin(object):
    form = movenodeform_factory(Personnel)
    object_list_template = 'admin/model_list.html'

xadmin.site.register(Personnel, PersonnelAdmin)
xadmin.site.register(Service)
xadmin.site.register(Fonction)
