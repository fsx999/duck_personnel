__author__ = 'paulguichon'
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Personnel, Service, Fonction


class PersonnelAdmin(TreeAdmin):
    form = movenodeform_factory(Personnel)


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Service)
admin.site.register(Fonction)
