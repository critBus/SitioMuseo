"""SitioMuseo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Aplicacion.views import *
urlpatterns = [
    path('', view_pagina_principal, name='pagina_principal'),
    path('admin/', admin.site.urls,name='admin'),
    path('quienes_somos/', view_quines_somos, name='quienes_somos'),
    path('menu/', view_menu_principal, name='menu'),
    path('sala_transitoria/', view_sala_transitoria, name='sala_transitoria'),
    path('descripcion_salas/', view_sala_normal, name='descripcion_salas'),
    path('trabajo_investigativo/', view_trabajo_investigativo, name='trabajo_investigativo'),
    path('galeria/', view_menu_galeria, name='galeria'),
    path('recorrido_virtual/', view_recorridos_virtuales, name='recorrido_virtual'),
    path('recorrido_interactivo/', view_recorrido_interactivo, name='recorrido_interactivo'),
    path('juegos_interactivo/', view_seleccionar_tipo_juegos, name='juegos_interactivo'),
    path('juegos_interactivo/marcar/lista/', view_lista_juegos_marcar, name='lista_juegos_marcar'),
    path('juegos_interactivo/marcar/id/<str:id>', view_juego_marcar),
    path('juegos_interactivo/verdadero_falso/lista/', view_seleccionar_tipo_juegos, name='lista_juegos_verdadero_falso'),

    path('galeria/galeria/', Articulos_ListView.as_view(), name='galeria_galeria'),
    path('galeria/vitrina/<str:id>', view_lista_vitrinas),#, name='galeria_vitrina'
    path('galeria/salas/vitrina/', view_lista_salas_para_vitrinas, name='galeria_vitrina'),#

    path('detalles_descripcion_salas/<str:id>', view_detalles_sala_normal),
    path('detalles_trabajo_investigativo/<str:id>', view_detalles_trabajo_investigativo),
    path('detalles_recorrido_interactivo/<str:id>', view_detalles_recorrido_interactivo),
    path('detalles_vitrinas/<str:id>', view_detalles_vitrina),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
