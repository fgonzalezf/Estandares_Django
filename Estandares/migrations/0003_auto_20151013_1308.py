# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estandares', '0002_documento_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='discucion',
            new_name='discusion',
        ),
    ]
