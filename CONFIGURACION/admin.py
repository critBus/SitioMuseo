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

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % \
                (image_url, image_url, file_name, ""))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

STYLES_FORMFIELDS={models.ImageField: {'widget': AdminImageWidget},#ImageUploaderWidget
                           models.TextField: {'widget': CKEditorWidget},
                           models.CharField: {'widget': TextInput(attrs={"size": "100"})}
                           }

class PaginaPrincipalAdmin(SingletonModelAdmin):
    model = PaginaPrincipal
    formfield_overrides = STYLES_FORMFIELDS


admin.site.register(PaginaPrincipal, PaginaPrincipalAdmin)

class ConfiguracionGeneralAdmin(SingletonModelAdmin):
    model = ConfiguracionGeneral
    formfield_overrides = STYLES_FORMFIELDS
admin.site.register(ConfiguracionGeneral, ConfiguracionGeneralAdmin)


class MenuPrincipalAdmin(SingletonModelAdmin):
    model = MenuPrincipal
    formfield_overrides = STYLES_FORMFIELDS


admin.site.register(MenuPrincipal, MenuPrincipalAdmin)