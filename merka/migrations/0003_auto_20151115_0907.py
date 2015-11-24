# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merka', '0002_auto_20151114_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='seccion',
            old_name='name',
            new_name='nombre',
        ),
    ]
