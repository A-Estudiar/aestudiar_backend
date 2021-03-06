from django.contrib.gis.db import models

class Escuela(models.Model):
  jurisdiccion = models.CharField(max_length=500, null=True)
  cue_anexo = models.IntegerField(null=True)
  nombre = models.CharField(max_length=400, null=True)
  sector = models.CharField(max_length=50, null=True)
  estado = models.CharField(max_length=50, null=True)
  domicilio = models.CharField(max_length=1000, null=True)
  cp = models.IntegerField(null=True)
  telefono = models.CharField(max_length=30, null=True)
  localidad = models.CharField(max_length=150, null=True)
  departamento = models.CharField(max_length=150, null=True)
  email = models.CharField(max_length=500, null=True)
  ed_comun = models.BooleanField(default=False)
  ed_especial = models.BooleanField(default=False)
  ed_jov_adu = models.BooleanField(default=False)
  ed_arte = models.BooleanField(default=False)
  ed_hosp_dom = models.BooleanField(default=False)
  ed_inter_bil = models.BooleanField(default=False)
  ed_encierro = models.BooleanField(default=False)
  ed_comun_jardin_mat = models.BooleanField(default=False)
  ed_comun_jardin_inf = models.BooleanField(default=False)
  ed_comun_primaria = models.BooleanField(default=False)
  ed_comun_secundaria = models.BooleanField(default=False)
  ed_comun_sec_tecnica = models.BooleanField(default=False)
  ed_comun_no_univ = models.BooleanField(default=False)
  ed_comun_no_univ_inet = models.BooleanField(default=False)
  ed_arte_secundaria = models.BooleanField(default=False)
  ed_arte_sup_no_univ = models.BooleanField(default=False)
  ed_arte_cursos_talleres = models.BooleanField(default=False)
  ed_esp_temprana = models.BooleanField(default=False)
  ed_esp_jardin_inf = models.BooleanField(default=False)
  ed_esp_primaria = models.BooleanField(default=False)
  ed_esp_secundaria = models.BooleanField(default=False)
  ed_esp_talleres = models.BooleanField(default=False)
  ed_j_a_primaria = models.BooleanField(default=False)
  ed_j_a_egb3 = models.BooleanField(default=False)
  ed_j_a_secundaria = models.BooleanField(default=False)
  ed_j_a_alfabetizacion = models.BooleanField(default=False)
  ed_j_a_form_prof = models.BooleanField(default=False)
  ed_j_a_form_prof_inet = models.BooleanField(default=False)
  ed_hosp_inicial = models.BooleanField(default=False)
  ed_hosp_primaria = models.BooleanField(default=False)
  ed_hosp_secundaria = models.BooleanField(default=False)
  servicios_comp = models.BooleanField(default=False)
  tipo_ubicacion = models.IntegerField(null=True)
  pos = models.PointField()
  
  objects = models.GeoManager()

class Encuesta(models.Model):
  escuela = models.ForeignKey('Escuela')
  created = models.DateTimeField(auto_now_add=True)
  infraestructura= models.IntegerField(null=True)
  calidadeducativa= models.IntegerField(null=True)
  cuota= models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Denuncia(models.Model):
  escuela = models.ForeignKey('Escuela')
  created = models.DateTimeField(auto_now_add=True)
  texto = models.TextField()
