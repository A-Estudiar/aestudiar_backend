# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0003_auto_20141031_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='lat',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='lon',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=9),
            preserve_default=True,
        ),
    ]
