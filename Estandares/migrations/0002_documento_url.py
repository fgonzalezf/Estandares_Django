# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estandares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='url',
            field=models.CharField(default='#', max_length=250),
            preserve_default=False,
        ),
    ]
