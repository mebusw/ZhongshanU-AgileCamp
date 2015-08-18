# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExchange', '0002_auto_20150818_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default=datetime.datetime(2015, 8, 18, 13, 11, 4, 523743, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
