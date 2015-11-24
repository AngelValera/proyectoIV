# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('merka', '0004_seccion_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 15, 9, 57, 44, 279137, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
