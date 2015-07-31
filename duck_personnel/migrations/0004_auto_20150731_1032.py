# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_personnel', '0003_auto_20150729_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='fonction_save',
            field=models.ForeignKey(related_name='fonctions_save', to='duck_personnel.Fonction', null=True),
        ),
        migrations.AddField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(to='duck_personnel.Service', null=True),
        ),
    ]
