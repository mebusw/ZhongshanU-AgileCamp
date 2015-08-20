# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExchange', '0005_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uname',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
