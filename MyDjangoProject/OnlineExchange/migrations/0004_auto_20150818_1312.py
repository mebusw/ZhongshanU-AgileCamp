# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExchange', '0003_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
