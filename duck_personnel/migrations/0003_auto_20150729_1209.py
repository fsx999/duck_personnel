# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('duck_personnel', '0002_auto_20150728_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonction',
            name='code',
            field=models.CharField(default='E', max_length=1, verbose_name='Code Employee', choices=[('R', 'Responsable'), ('E', 'Normale')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='duck_personnel.Service', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='tree_id',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
