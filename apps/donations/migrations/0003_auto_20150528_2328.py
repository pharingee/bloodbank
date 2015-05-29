# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20150528_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='number',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
