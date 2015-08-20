# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='kind',
            field=models.CharField(default=datetime.datetime(2015, 8, 18, 15, 38, 19, 602000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
