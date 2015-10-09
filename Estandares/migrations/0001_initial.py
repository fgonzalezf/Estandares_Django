# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('fechaPublicacion', models.DateField()),
                ('vigencia', models.DateField()),
                ('otrasVersiones', models.CharField(max_length=100)),
                ('discucion', models.CharField(max_length=100)),
            ],
        ),
    ]
