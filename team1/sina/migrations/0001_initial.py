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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('_usr', models.CharField(max_length=30)),
                ('_pwd', models.CharField(max_length=30)),
                ('_mail', models.CharField(max_length=40)),
            ],
        ),
    ]
