# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=120, verbose_name='Role')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=30, verbose_name='Pr\xe9nom')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='T\xe9l\xe9phone')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('fonction', models.ForeignKey(to='duck_personnel.Fonction')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='duck_personnel.Personnel', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=120, verbose_name='Pole')),
            ],
        ),
        migrations.AddField(
            model_name='fonction',
            name='service',
            field=models.ForeignKey(to='duck_personnel.Service'),
        ),
    ]
