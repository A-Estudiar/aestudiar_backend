from django.http import HttpResponse, HttpResponseNotFound
import json
from decimal import Decimal

from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D

from api_aestudiar.models import Escuela, Encuesta, Denuncia

from api_aestudiar.utils import DecimalEncoder

def short_escuela(d):
  return {'id': d.id,
		'nombre': d.nombre,
		'lat': d.pos.y,
		'lon': d.pos.x,
		'sector': d.sector,
		'ed_comun': d.ed_comun,
		'ed_especial': d.ed_especial,
		'ed_jov_adu': d.ed_jov_adu,
		'ed_arte': d.ed_arte,
		'ed_hosp_dom': d.ed_hosp_dom,
		'ed_inter_bil': d.ed_inter_bil,
		'ed_encierro': d.ed_encierro
  }

def detail_escuela(d):
  Encuestas = Encuesta.objects.filter(escuela_id=d.id)

  num_encuestas = len(Encuestas)
  sum_infraestructura = Decimal(0)
  sum_calidadeducativa = Decimal(0)
  sum_cuota = Decimal(0)
  for row in Encuestas:
	sum_infraestructura += row.infraestructura
	sum_calidadeducativa += row.calidadeducativa
	sum_cuota += row.cuota

  avg_infraestructura = None
  avg_calidadeducativa = None
  avg_cuota = None

  if num_encuestas > 0:
	avg_infraestructura = sum_infraestructura / num_encuestas
	avg_calidadeducativa = sum_calidadeducativa / num_encuestas
	avg_cuota = sum_cuota / num_encuestas

  Denuncias = Denuncia.objects.filter(escuela_id=d.id)

  d_arr = []

  for row in Denuncias:
	d_arr.append(row.texto)

  return {
  'id': d.id,
  'jurisdiccion': d.jurisdiccion,
  'cue_anexo': d.cue_anexo,
  'nombre': d.nombre,
  'sector': d.sector,
  'estado': d.estado,
  'domicilio': d.domicilio,
  'cp': d.cp,
  'telefono': d.telefono,
  'localidad': d.localidad,
  'departamento': d.departamento,
  'email': d.email,
  'ed_comun': d.ed_comun,
  'ed_especial': d.ed_especial,
  'ed_jov_adu': d.ed_jov_adu,
  'ed_arte': d.ed_arte,
  'ed_hosp_dom': d.ed_hosp_dom,
  'ed_inter_bil': d.ed_inter_bil,
  'ed_encierro': d.ed_encierro,
  'ed_comun_jardin_mat': d.ed_comun_jardin_mat,
  'ed_comun_jardin_inf': d.ed_comun_jardin_inf,
  'ed_comun_primaria': d.ed_comun_primaria,
  'ed_comun_secundaria': d.ed_comun_secundaria,
  'ed_comun_sec_tecnica': d.ed_comun_sec_tecnica,
  'ed_comun_no_univ': d.ed_comun_no_univ,
  'ed_comun_no_univ_inet': d.ed_comun_no_univ_inet,
  'ed_arte_secundaria': d.ed_arte_secundaria,
  'ed_arte_sup_no_univ': d.ed_arte_sup_no_univ,
  'ed_arte_cursos_talleres': d.ed_arte_cursos_talleres,
  'ed_esp_temprana': d.ed_esp_temprana,
  'ed_esp_jardin_inf': d.ed_esp_jardin_inf,
  'ed_esp_primaria': d.ed_esp_primaria,
  'ed_esp_secundaria': d.ed_esp_secundaria,
  'ed_esp_talleres': d.ed_esp_talleres,
  'ed_j_a_primaria': d.ed_j_a_primaria,
  'ed_j_a_egb3': d.ed_j_a_egb3,
  'ed_j_a_secundaria': d.ed_j_a_secundaria,
  'ed_j_a_alfabetizacion': d.ed_j_a_alfabetizacion,
  'ed_j_a_form_prof': d.ed_j_a_form_prof,
  'ed_j_a_form_prof_inet': d.ed_j_a_form_prof_inet,
  'ed_hosp_inicial': d.ed_hosp_inicial,
  'ed_hosp_primaria': d.ed_hosp_primaria,
  'ed_hosp_secundaria': d.ed_hosp_secundaria,
  'servicios_comp': d.servicios_comp,
  'tipo_ubicacion': d.tipo_ubicacion,
  'lat': d.pos.y,
  'lon': d.pos.x,
  'avg_infraestructura': avg_infraestructura,
  'avg_calidadeducativa': avg_calidadeducativa,
  'avg_cuota': avg_cuota,
  'denuncias': d_arr
  }

def all_escuelas(request, lon, lat):
  ref_pnt = fromstr("POINT(%s %s)" % (lon, lat))
  distance_from_point = {'m':'5000'}
  escuelas_nearby = Escuela.objects.filter(pos__distance_lte=(ref_pnt, D(**distance_from_point) )).distance(ref_pnt).order_by('distance')[0:150]

  all_escuelas = map(short_escuela, escuelas_nearby)

  return HttpResponse(json.dumps(all_escuelas, cls=DecimalEncoder), content_type="application/json")

def escuela(request, id):
  try:
	escuela = Escuela.objects.get(pk=id)
  except Escuela.DoesNotExist:
	return HttpResponseNotFound()

  return HttpResponse(json.dumps(detail_escuela(escuela), cls=DecimalEncoder), content_type="application/json")

def puntuar(request, id):
  try:
	escuela = Escuela.objects.get(pk=id)
  except Escuela.DoesNotExist:
	return HttpResponseNotFound()

  obj = json.loads(request.body)

  enc = Encuesta()
  enc.escuela = escuela
  enc.infraestructura = obj['puntuar_infraestructura']
  enc.calidadeducativa = obj['puntuar_calidadeducativa']
  enc.cuota = obj['puntuar_cuota']
  enc.save()

  return HttpResponse(json.dumps(detail_escuela(escuela), cls=DecimalEncoder), content_type="application/json")

def denunciar(request, id):
  try:
	escuela = Escuela.objects.get(pk=id)
  except Escuela.DoesNotExist:
	return HttpResponseNotFound()

  obj = json.loads(request.body)

  den = Denuncia()
  den.escuela = escuela
  den.texto = obj['denuncia']
  den.save()

  return HttpResponse(json.dumps(detail_escuela(escuela), cls=DecimalEncoder), content_type="application/json")
