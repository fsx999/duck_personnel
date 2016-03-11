# coding=utf-8
from django.apps import AppConfig


class DuckPersonnel(AppConfig):
    name = "duck_personnel"
    label = "duck_personnel"

    collapse_settings = [{
        "group_label": "Duck_Personnel",
        "icon": 'fa-fw fa fa-circle-o',
        "entries": [{
            "label": 'Personnels ',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_personnel/personnel/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Services',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_personnel/service/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Fonctions',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_personnel/fonction/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, ]