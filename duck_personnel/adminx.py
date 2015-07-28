__author__ = 'paulguichon'

from .models import Personnel, Service, Fonction
import xadmin

class PersonnelAdmin(object):
    object_list_template = 'admin/model_list.html'


xadmin.site.register(Personnel, PersonnelAdmin)
xadmin.site.register(Service)
xadmin.site.register(Fonction)
