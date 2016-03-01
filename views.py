# coding=utf-8
from __future__ import unicode_literals
import csv
from django.http import HttpResponse
from django.views.generic import View
from rest_framework import viewsets, filters, permissions
import xlwt
from .models import Service, Fonction, Personnel
from .serializers import ServiceSerizalizer, FonctionSerizalizer, PersonnelSerizalizer
__author__ = 'paulguichon'


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerizalizer
    permission_classes = [permissions.AllowAny]


class FonctionViewSet(viewsets.ModelViewSet):
    queryset = Fonction.objects.all()
    serializer_class = FonctionSerizalizer
    permission_classes = [permissions.AllowAny]


class PersonnelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Personnel.objects.all().prefetch_related('fonction')
    serializer_class = PersonnelSerizalizer
    filter_fields = ('service', )


class ExportFile(View):
    fields = ['Nom', 'Prenom', 'Service', 'Email', 'Telephone', 'Bureau', 'Fonctions']

    def get_csv(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=annuaire.csv'

        writer = csv.writer(response)
        writer.writerow(self.fields)
        for x in Personnel.objects.all().prefetch_related('fonction'):
            writer.writerow(x.get_fields_list)
        return response

    def get_excel(self):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=export.xls'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('etudiant')

        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold = True
        style.font = font

        for j, field in enumerate(self.fields):
            ws.write(0, j, field, style=style)

        personnnel = Personnel.objects.all().prefetch_related('fonction')
        for i, person in enumerate(personnnel):
            for j, field in enumerate(person.get_fields_list):
                ws.write(i + 1, j, field)
        wb.save(response)

        return response

    def get(self, request, *args, **kwargs):
        if request.GET.get('type', 'csv') == 'csv':
            return self.get_csv()
        else:
            return self.get_excel()


