# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jurisdiccion', models.CharField(max_length=200)),
                ('cue_anexo', models.IntegerField()),
                ('nombre', models.CharField(max_length=400)),
                ('sector', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=1000)),
                ('cp', models.IntegerField()),
                ('telefono', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('ed_comun', models.BooleanField(default=False)),
                ('ed_especial', models.BooleanField(default=False)),
                ('ed_jov_adu', models.BooleanField(default=False)),
                ('ed_arte', models.BooleanField(default=False)),
                ('ed_hosp_dom', models.BooleanField(default=False)),
                ('ed_inter_bil', models.BooleanField(default=False)),
                ('ed_encierro', models.BooleanField(default=False)),
                ('ed_comun_jardin_mat', models.BooleanField(default=False)),
                ('ed_comun_jardin_inf', models.BooleanField(default=False)),
                ('ed_comun_primaria', models.BooleanField(default=False)),
                ('ed_comun_secundaria', models.BooleanField(default=False)),
                ('ed_comun_sec_tecnica', models.BooleanField(default=False)),
                ('ed_comun_no_univ', models.BooleanField(default=False)),
                ('ed_comun_no_univ_inet', models.BooleanField(default=False)),
                ('ed_arte_secundaria', models.BooleanField(default=False)),
                ('ed_arte_sup_no_univ', models.BooleanField(default=False)),
                ('ed_arte_cursos_talleres', models.BooleanField(default=False)),
                ('ed_esp_temprana', models.BooleanField(default=False)),
                ('ed_esp_jardin_inf', models.BooleanField(default=False)),
                ('ed_esp_primaria', models.BooleanField(default=False)),
                ('ed_esp_secundaria', models.BooleanField(default=False)),
                ('ed_esp_talleres', models.BooleanField(default=False)),
                ('ed_j_a_primaria', models.BooleanField(default=False)),
                ('ed_j_a_egb3', models.BooleanField(default=False)),
                ('ed_j_a_secundaria', models.BooleanField(default=False)),
                ('ed_j_a_alfabetizacion', models.BooleanField(default=False)),
                ('ed_j_a_form_prof', models.BooleanField(default=False)),
                ('ed_j_a_form_prof_inet', models.BooleanField(default=False)),
                ('ed_hosp_inicial', models.BooleanField(default=False)),
                ('ed_hosp_primaria', models.BooleanField(default=False)),
                ('ed_hosp_secundaria', models.BooleanField(default=False)),
                ('servicios_comp', models.BooleanField(default=False)),
                ('tipo_ubicacion', models.IntegerField()),
                ('lat', models.IntegerField()),
                ('lon', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
