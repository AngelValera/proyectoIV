# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=128, unique=True, serialize=False, primary_key=True)),
                ('precio', models.IntegerField(default=0)),
                ('imagen', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('nombre', models.CharField(max_length=128, unique=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='seccion',
            field=models.ForeignKey(to='merka.Seccion'),
        ),
    ]
