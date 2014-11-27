# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields

class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0008_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='pos',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='escuela',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='escuela',
            name='lon',
        ),
    ]
