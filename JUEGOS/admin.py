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


class RespuestaInline(NestedStackedInline):#NestedStackedInline
    model = Respuesta
    extra = 1
    fk_name = 'pregunta'
    formfield_overrides = STYLES_FORMFIELDS

class PreguntaInline(NestedStackedInline):#NestedStackedInline
    model = Pregunta
    extra = 1
    fk_name = 'juego'
    inlines = [RespuestaInline]
    formfield_overrides = STYLES_FORMFIELDS

class JuegoAdmin(NestedModelAdmin):
    model = JuegoMarcar
    inlines =[PreguntaInline]
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(JuegoMarcar,JuegoAdmin)