# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0006_encuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='calidadeducativa',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encuesta',
            name='cuota',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encuesta',
            name='infraestructura',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
