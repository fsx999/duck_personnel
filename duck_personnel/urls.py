__author__ = 'paulguichon'
from django.conf.urls import url, include
from . import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'fonction', views.FonctionViewSet)
router.register(r'personnels', views.PersonnelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
