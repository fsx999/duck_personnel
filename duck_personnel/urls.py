# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import url, include
from . import views
from rest_framework import routers

__author__ = 'paulguichon'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'services', views.ServiceViewSet)
router.register(r'fonction', views.FonctionViewSet)
router.register(r'personnels', views.PersonnelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
