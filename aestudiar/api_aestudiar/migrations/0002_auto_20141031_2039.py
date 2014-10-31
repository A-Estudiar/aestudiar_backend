# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='lat',
            field=models.DecimalField(max_digits=12, decimal_places=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='lon',
            field=models.DecimalField(max_digits=12, decimal_places=9),
            preserve_default=True,
        ),
    ]
