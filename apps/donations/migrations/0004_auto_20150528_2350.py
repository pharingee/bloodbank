# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20150528_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='date_taken',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blood',
            name='hospital',
            field=models.ForeignKey(related_name='bloods', blank=True, to='users.Hospital', null=True),
            preserve_default=True,
        ),
    ]
