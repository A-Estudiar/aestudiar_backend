from django.http import HttpResponse
import json
from decimal import Decimal 

from api_aestudiar.models import Escuela

from api_aestudiar.utils import DecimalEncoder

def short_escuela(d):
  return {'id': d.id,
        'nombre': d.nombre,
        'lat': d.lat,
        'lon': d.lon}

def detail_escuela(d):
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
  'lat': d.lat,
  'lon': d.lon
  }

def all_escuelas(request):
  all_escuelas = map(short_escuela, Escuela.objects.all()[:5000])

  return HttpResponse(json.dumps(all_escuelas, cls=DecimalEncoder), content_type="application/json")

def escuela(request, id):
  try:
    escuela = Escuela.objects.get(pk=id)
  except Escuela.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  return HttpResponse(json.dumps(detail_escuela(escuela), cls=DecimalEncoder), content_type="application/json")