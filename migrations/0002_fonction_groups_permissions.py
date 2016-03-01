# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('duck_personnel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonction',
            name='groups_permissions',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
