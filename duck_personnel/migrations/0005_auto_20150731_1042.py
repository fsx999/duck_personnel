# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_personnel', '0004_auto_20150731_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='fonction',
        ),
        migrations.AddField(
            model_name='personnel',
            name='fonction',
            field=models.ManyToManyField(to='duck_personnel.Fonction', null=True),
        ),
    ]
