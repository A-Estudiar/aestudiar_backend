# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0010_auto_20141127_1518'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='escuela',
            name='pos',
        ),
        migrations.AddField(
            model_name='escuela',
            name='pos',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
    ]
