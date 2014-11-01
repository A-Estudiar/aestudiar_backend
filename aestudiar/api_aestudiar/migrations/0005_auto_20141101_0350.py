# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0004_auto_20141031_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='email',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='jurisdiccion',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
