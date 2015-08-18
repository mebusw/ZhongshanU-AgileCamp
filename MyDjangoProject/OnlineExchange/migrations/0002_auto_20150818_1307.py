# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.IntegerField()),
                ('pid', models.IntegerField(serialize=False, primary_key=True)),
                ('pname', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.BinaryField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
