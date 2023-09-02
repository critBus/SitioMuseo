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


class Trabajo_InvestigativoAdmin(admin.ModelAdmin):
    model = Trabajo_Investigativo
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Trabajo_Investigativo,Trabajo_InvestigativoAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(Articulo,ArticuloAdmin)