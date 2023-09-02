from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from CONFIGURACION.models import *
from SALAS.models import *
from TRABAJOS_INVESTIGATIVOS.models import *
from Aplicacion.UtilesAplicacion.ClasesLogica import *
from django.views import generic
from JUEGOS.models import *

def view_pagina_principal(request):
    config = ConfiguracionGeneral.get_solo()
    datos = PaginaPrincipal.get_solo()
    return render(request,'index.html', {'config': config,"datos":datos})

def view_quines_somos(request):
    config = ConfiguracionGeneral.get_solo()
    return render(request,'quienes_somos.html', {'config': config})


def view_menu_principal(request):
    config = ConfiguracionGeneral.get_solo()
    datos = MenuPrincipal.get_solo()
    return render(request,'menu.html', {'config': config,"datos":datos})

def view_menu_galeria(request):
    config = ConfiguracionGeneral.get_solo()
    return render(request,'menu_galeria.html', {'config': config})

def view_sala_transitoria(request):
    config = ConfiguracionGeneral.get_solo()


    listaDeItems = []
    l = Sala_Transitoria.objects.all()
    for i,e in enumerate(l):
        item = ItemDeLista()
        item.Nombre = e.Nombre
        item.Descripcion = e.Descripcion
        if item.Descripcion is None:
            item.Descripcion = ""
        item.Imagen = e.Imagen
        item.id = e.id
        item.indice=i
        listaDeItems.append(item)

    return render(request,'sala_transitoria.html', {'config': config,'lista': listaDeItems})



def view_sala_normal(request):
    config = ConfiguracionGeneral.get_solo()


    listaDeItems = []
    l =Recorrido_Interactivo.objects.all() #Sala_Normal.objects.all()
    for i,e in enumerate(l):
        item = ItemDeLista()
        item.Nombre = e.Nombre
        item.Descripcion = e.Descripcion
        if item.Descripcion is None:
            item.Descripcion = ""
        item.Imagen = e.Imagen
        item.id = e.id
        item.indice=i
        listaDeItems.append(item)

    return render(request,'sala_normal.html', {'config': config,'lista': listaDeItems})


def view_detalles_sala_normal(request,id):
    config = ConfiguracionGeneral.get_solo()
    e =Recorrido_Interactivo.objects.filter(id=id).first() #Sala_Normal.objects.filter(id=id).first()
    item = ItemDeLista()
    item.Nombre = e.Nombre
    item.Descripcion =e.Descripcion #contenido
    return render(request,'Vista_Detalle_sala_normal.html', {'config': config,"item":item})










def view_trabajo_investigativo(request):
    config = ConfiguracionGeneral.get_solo()


    listaDeItems = []
    l = Trabajo_Investigativo.objects.all()
    for i,e in enumerate(l):
        item = ItemDeLista()
        item.Nombre = e.Nombre
        item.Descripcion = e.Descripcion
        if item.Descripcion is None:
            item.Descripcion = ""
        item.Imagen = e.Imagen
        item.id = e.id
        item.indice=i
        listaDeItems.append(item)

    return render(request,'trabajos_investigativos.html', {'config': config,'lista': listaDeItems})


def view_detalles_trabajo_investigativo(request,id):
    config = ConfiguracionGeneral.get_solo()
    e = Trabajo_Investigativo.objects.filter(id=id).first()
    item = ItemDeLista()
    item.Nombre = e.Nombre
    item.Descripcion =e.Descripcion #contenido
    return render(request,'Vista_Detalle_sala_normal.html', {'config': config,"item":item})





def view_recorrido_interactivo(request):
    config = ConfiguracionGeneral.get_solo()


    listaDeItems = []
    l = Recorrido_Interactivo.objects.all()
    for i,e in enumerate(l):
        item = ItemDeLista()
        item.Nombre = e.Nombre

        item.Imagen = e.Imagen
        item.id = e.id
        item.indice=i
        listaDeItems.append(item)

    return render(request,'recorrido_interactivo.html', {'config': config,'lista': listaDeItems})


def view_detalles_recorrido_interactivo(request,id):
    config = ConfiguracionGeneral.get_solo()
    recorrido = Recorrido_Interactivo.objects.filter(id=id).first()

    listaDeItems = []
    l = ImagenesRecorrido_Interactivo.objects.filter(Recorrido_Interactivo=recorrido)
    for i, e in enumerate(l):
        item = ItemDeLista()
        item.Imagen = e.Imagen
        item.id = e.id
        item.indice = i
        listaDeItems.append(item)

    return render(request, 'recorriodos_por_las_salas_imagenes.html', {'config': config, 'lista': listaDeItems})


def view_lista_salas_para_vitrinas(request):
    config = ConfiguracionGeneral.get_solo()


    listaDeItems = []
    l = Recorrido_Interactivo.objects.all()
    for i,e in enumerate(l):
        item = ItemDeLista()
        item.Nombre = e.Nombre

        item.Imagen = e.Imagen
        item.id = e.id
        item.indice=i
        listaDeItems.append(item)

    return render(request,'salas_para_vitrinas.html', {'config': config,'lista': listaDeItems})





def view_lista_vitrinas(request,id):
    config = ConfiguracionGeneral.get_solo()
    lista = Vitrina.objects.filter(Recorrido_Interactivo=Recorrido_Interactivo.objects.get(id=id))
    return render(request,'lista_vitrinas.html', {'config': config,"lista":lista})



def view_detalles_vitrina(request,id):
    config = ConfiguracionGeneral.get_solo()

    e = Vitrina.objects.filter(id=id).first()

    item = ItemDeLista()
    item.Imagen = e.Imagen
    item.id = e.id
    item.Descripcion=e.Descripcion


    return render(request, 'detalles_vitrinas.html', {'config': config, 'item': item})


class Articulos_ListView(generic.ListView):
    model = Articulo

    template_name = "lista_articulos.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Nombre__icontains=q)
        return queryset
    def get_context_data(self, *a, object_list=None, **kwargs):
        context=super().get_context_data(*a,object_list=object_list,**kwargs)
        config = ConfiguracionGeneral.get_solo()
        context['config']=config

        return context

def view_recorridos_virtuales(request):
    config = ConfiguracionGeneral.get_solo()
    lista = RecorridoVirtual.objects.all()
    return render(request,'lista_recorrido_virtual.html', {'config': config,"lista":lista})


def view_lista_juegos_marcar(request):
    config = ConfiguracionGeneral.get_solo()
    lista = JuegoMarcar.objects.all()
    return render(request,'lista_juegos_marcar.html', {'config': config,"lista":lista})


def view_juego_marcar(request,id):
    config = ConfiguracionGeneral.get_solo()
    dato = JuegoMarcar.objects.filter(id=id).first()
    return render(request,'juego_marcar_pregunta.html', {'config': config,"dato":dato})



def view_seleccionar_tipo_juegos(request):
    config = ConfiguracionGeneral.get_solo()
    return render(request,'seleccionar_tipo_juego.html', {'config': config})