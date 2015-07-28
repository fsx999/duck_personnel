from django.contrib.admin.utils import quote
from django_mptt_admin import util
from django.core.urlresolvers import reverse
__author__ = 'paulguichon'
from django.contrib import admin

from .models import Personnel, Service, Fonction
from django_mptt_admin.admin import DjangoMpttAdmin

class PersonnelAdmin(DjangoMpttAdmin):
    # /admin/duck_personnel/personnel/tree_json/
    def get_tree_data(self, qs, max_level):
        pk_attname = self.model._meta.pk.attname

        def handle_create_node(instance, node_info):
            pk = quote(getattr(instance, pk_attname))
            node_info.update(
                # url=self.get_admin_url('change', (quote(pk),)),
                url=reverse('xadmin:duck_personnel_personnel_change', args=(quote(pk),)),
                move_url=self.get_admin_url('move', (quote(pk),))
            )

        return util.get_tree_from_queryset(qs, handle_create_node, max_level)


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Service)
admin.site.register(Fonction)
