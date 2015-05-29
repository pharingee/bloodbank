# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_due', models.DateTimeField()),
                ('text', models.TextField()),
                ('hospital', models.ForeignKey(related_name='notifications', to='users.Hospital')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
