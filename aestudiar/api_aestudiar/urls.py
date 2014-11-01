from django.conf.urls import patterns, url

from api_aestudiar import api

urlpatterns = patterns('',    
    url(r'^all_escuelas$', api.all_escuelas, name='api_all_escuelas'),
    url(r'^escuela/(\d+)$', api.escuela, name='api_escuela'),
    url(r'^escuela/(\d+)/puntuar$', api.puntuar, name='api_escuela_puntuar'),
    url(r'^escuela/(\d+)/denunciar$', api.denunciar, name='api_escuela_denunciar')
)