from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.residente_list, name='residente_list'),
    url(r'^residente/(?P<pk>[0-9]+)/$', views.residente_detail,  name='residente_detail'),
    url(r'^residente/new/$', views.residente_new, name='residente_new'),
    url(r'^residente/(?P<pk>[0-9]+)/edit/$', views.residente_edit, name='residente_edit'),
    url(r'^residente/(?P<pk>\d+)/remove/$', views.residente_remove, name='residente_remove'),

    url(r'^mes/$', views.mes_list, name='mes_list'),
    url(r'^mes/(?P<pk>[0-9]+)/$', views.mes_detail,  name='mes_detail'),
    url(r'^mes/new/$', views.mes_new, name='mes_new'),
    url(r'^mes/(?P<pk>[0-9]+)/edit/$', views.mes_edit, name='mes_edit'),
    url(r'^mes/(?P<pk>\d+)/remove/$', views.mes_remove, name='mes_remove'),

    url(r'^pago/$', views.pago_list, name='pago_list'),
    url(r'^pago/new/$', views.pago_new, name='pago_new'),
    url(r'^pago/$', views.pago_list, name='pago_list'),

    url(r'^factura/$', views.factura_list, name='factura_list'),
    #url(r'^accounts/', include('registration.urls')),
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #url(r'^pago/nuevo/$', views.pago_nuevo, name='pago_nuevo'),
]
