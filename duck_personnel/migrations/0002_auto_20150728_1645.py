# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('duck_personnel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='bureau',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fonction',
            name='label',
            field=models.CharField(max_length=120, verbose_name='Fonction'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='phone',
            field=models.CharField(max_length=10, null=True, verbose_name='T\xe9l\xe9phone', blank=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='label',
            field=models.CharField(max_length=120, verbose_name='Service'),
        ),
    ]
