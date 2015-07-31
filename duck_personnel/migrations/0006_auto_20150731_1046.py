# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_personnel', '0005_auto_20150731_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fonction',
            name='service',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='fonction_save',
        ),
    ]
