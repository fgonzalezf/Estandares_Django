# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estandares', '0003_auto_20151013_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Versiones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('url', models.CharField(max_length=250)),
                ('codigo', models.ManyToManyField(to='Estandares.Documento')),
            ],
        ),
    ]
