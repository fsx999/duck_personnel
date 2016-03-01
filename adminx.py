from django.views.decorators.cache import never_cache
from xadmin.views import filter_hook

__author__ = 'paulguichon'

from .models import Personnel, Service, Fonction
import xadmin
from xadmin import views

class PersonnelAdmin(object):
    object_list_template = 'admin/model_list.html'


class OrganigrammeView(views.Dashboard):
    base_template = 'duck_personnel/organigramme.html'
    widget_customiz = False

    def get_context(self):
        context = super(OrganigrammeView, self).get_context()
        context['personnes'] = Personnel.objects.root_nodes()
        return context

    @filter_hook
    def get_breadcrumb(self):
        return [{'url': self.get_admin_url('index'), 'title': 'Accueil'},]

    @never_cache
    def get(self, request, *args, **kwargs):
        self.widgets = self.get_widgets()
        return self.template_response(self.base_template, self.get_context())

xadmin.site.register_view(r'^organigramme_view/$', OrganigrammeView, 'organigramme_view')

xadmin.site.register(Personnel, PersonnelAdmin)
xadmin.site.register(Service)
xadmin.site.register(Fonction)
