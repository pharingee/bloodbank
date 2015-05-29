# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20150528_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='number',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
