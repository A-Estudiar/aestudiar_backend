# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0002_auto_20141031_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='cp',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='cue_anexo',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='departamento',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='domicilio',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='email',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='estado',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='jurisdiccion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='localidad',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='nombre',
            field=models.CharField(max_length=400, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='sector',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='telefono',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='escuela',
            name='tipo_ubicacion',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
