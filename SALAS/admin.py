from django.forms import ClearableFileInput,TextInput
from django.contrib.admin.widgets import AdminFileWidget, FilteredSelectMultiple
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget


from image_uploader_widget.widgets import ImageUploaderWidget
from solo.admin import SingletonModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline

from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from django.contrib.admin.widgets import AdminFileWidget
from .models import *

from CONFIGURACION.admin import *


# class Sala_NormalAdmin(admin.ModelAdmin):
#     model = Sala_Normal
#     formfield_overrides = STYLES_FORMFIELDS
# admin.site.register(Sala_Normal,Sala_NormalAdmin)

class Sala_TransitoriaAdmin(admin.ModelAdmin):
    model = Sala_Transitoria
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Sala_Transitoria,Sala_TransitoriaAdmin)

class Articulo_IndependienteAdmin(admin.ModelAdmin):
    model = Articulo_Independiente
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Articulo_Independiente,Articulo_IndependienteAdmin)

class ImagenesRecorrido_InteractivoInline(NestedStackedInline):#NestedStackedInline
    model = ImagenesRecorrido_Interactivo
    extra = 1
    fk_name = 'Recorrido_Interactivo'
    formfield_overrides = STYLES_FORMFIELDS

# class Articulo_VitrinaInline(NestedStackedInline):#NestedStackedInline
#     model = Articulo_Vitrina
#     extra = 1
#     fk_name = 'Vitrina'
#     formfield_overrides = STYLES_FORMFIELDS

class VitrinaInline(NestedStackedInline):#NestedStackedInline
    model = Vitrina
    extra = 1
    fk_name = 'Recorrido_Interactivo'
    formfield_overrides = STYLES_FORMFIELDS
    # inlines = [Articulo_VitrinaInline]

class Recorrido_InteractivoAdmin(NestedModelAdmin):
    model = Recorrido_Interactivo
    inlines = [ImagenesRecorrido_InteractivoInline,VitrinaInline]
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Recorrido_Interactivo,Recorrido_InteractivoAdmin)


class ImagenesGaleriaInline(NestedStackedInline):#NestedStackedInline
    model = ImagenesGaleria
    extra = 1
    fk_name = 'Galeria'
    formfield_overrides = STYLES_FORMFIELDS

class GaleriaAdmin(admin.ModelAdmin):
    model = Galeria
    inlines =[ImagenesGaleriaInline]
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Galeria,GaleriaAdmin)


class RecorridoVirtualAdmin(admin.ModelAdmin):
    model = RecorridoVirtual
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(RecorridoVirtual,RecorridoVirtualAdmin)

