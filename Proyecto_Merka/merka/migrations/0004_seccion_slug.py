# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('merka', '0003_auto_20151115_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 15, 9, 43, 36, 820646, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
