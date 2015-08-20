# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_toWhere', models.CharField(max_length=50)),
                ('_when', models.CharField(max_length=50)),
                ('_peopleAmount', models.CharField(max_length=50)),
                ('_fromWhere', models.CharField(max_length=50)),
                ('_budget', models.CharField(max_length=50)),
                ('_otherRequest', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_question', models.CharField(max_length=20000)),
                ('_comment', models.CharField(max_length=20000)),
            ],
        ),
    ]
