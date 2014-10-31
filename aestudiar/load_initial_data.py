from api_aestudiar.models import Escuela
from decimal import Decimal

def transf_int(s):
  try:
    return int(s)
  except Exception:
    return None

def transf_bool(x):
  if x == 'x':
    return True
  else:
    return False

import csv
with open('../establecimientos.csv') as f:
  estreader=csv.reader(f, delimiter=',')
  for row in estreader:
    e = Escuela()
    e.jurisdiccion = row[0]
    e.cue_anexo = transf_int(row[1])
    e.nombre = row[2]
    e.sector = row[3]
    e.estado = row[4]
    e.domicilio = row[5]
    e.cp = transf_int(row[6])
    e.telefono = row[7]
    e.localidad = row[8]
    e.departamento = row[9]
    e.email = row[10]
    e.ed_comun = transf_bool(row[11])
    e.ed_especial = transf_bool(row[12])
    e.ed_jov_adu = transf_bool(row[13])
    e.ed_arte = transf_bool(row[14])
    e.ed_hosp_dom = transf_bool(row[15])
    e.ed_inter_bil = transf_bool(row[16])
    e.ed_encierro = transf_bool(row[17])
    e.ed_comun_jardin_mat = transf_bool(row[18])
    e.ed_comun_jardin_inf = transf_bool(row[19])
    e.ed_comun_primaria = transf_bool(row[20])
    e.ed_comun_secundaria = transf_bool(row[21])
    e.ed_comun_sec_tecnica = transf_bool(row[22])
    e.ed_comun_no_univ = transf_bool(row[23])
    e.ed_comun_no_univ_inet = transf_bool(row[24])
    e.ed_arte_secundaria = transf_bool(row[25])
    e.ed_arte_sup_no_univ = transf_bool(row[26])
    e.ed_arte_cursos_talleres = transf_bool(row[27])
    e.ed_esp_temprana = transf_bool(row[28])
    e.ed_esp_jardin_inf = transf_bool(row[29])
    e.ed_esp_primaria = transf_bool(row[30])
    e.ed_esp_secundaria = transf_bool(row[31])
    e.ed_esp_talleres = transf_bool(row[32])
    e.ed_j_a_primaria = transf_bool(row[33])
    e.ed_j_a_egb3 = transf_bool(row[34])
    e.ed_j_a_secundaria = transf_bool(row[35])
    e.ed_j_a_alfabetizacion = transf_bool(row[36])
    e.ed_j_a_form_prof = transf_bool(row[37])
    e.ed_j_a_form_prof_inet = transf_bool(row[38])
    e.ed_hosp_inicial = transf_bool(row[39])
    e.ed_hosp_primaria = transf_bool(row[40])
    e.ed_hosp_secundaria = transf_bool(row[41])
    e.servicios_comp = transf_bool(row[42])
    e.tipo_ubicacion = transf_int(row[43])
    e.lat = None
    e.lon = None
    try:
      e.lat = Decimal(row[44])
      e.lon = Decimal(row[45])
    except Exception:
      pass
    e.save()