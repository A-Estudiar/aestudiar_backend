# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_aestudiar', '0007_auto_20141101_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('escuela', models.ForeignKey(to='api_aestudiar.Escuela')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
