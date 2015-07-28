# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=30, verbose_name='Pr\xe9nom')),
                ('fonction', models.ForeignKey(to='duck_personnel.Fonction')),
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
