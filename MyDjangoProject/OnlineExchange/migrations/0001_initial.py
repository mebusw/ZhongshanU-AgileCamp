# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=15)),
                ('mail', models.CharField(max_length=20)),
                ('uid', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
