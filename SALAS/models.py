from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from django.utils.html import format_html
# Create your models here.

from solo.models import SingletonModel

from django.core.validators import RegexValidator
from django.forms import TextInput

from PIL import Image

RESOLUCION_W=800
RESOLUCION_H=800

# class Sala_Normal(models.Model):
#     class Meta:
#         verbose_name = 'Sala Normal'
#         verbose_name_plural = 'Salas Normales'
#
#     Nombre = models.CharField(max_length=50)
#     Descripcion = models.TextField()
#     Imagen = models.ImageField(upload_to='Sala_Normal')
#
#     def __str__(self):
#         return self.Nombre



class Sala_Transitoria(models.Model):
    class Meta:
        verbose_name = 'Sala Transitoria'
        verbose_name_plural = 'Salas Transitorias'

    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='Sala_Transitoria')

    def __str__(self):
        return self.Nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Imagen.path)
        if img.width > RESOLUCION_W or img.height > RESOLUCION_H:
            output_size = (RESOLUCION_W, RESOLUCION_H)
            img.thumbnail(output_size)
            img.save(self.Imagen.path)




class Recorrido_Interactivo(models.Model):
    class Meta:
        verbose_name = 'Recorrido Interactivo'
        verbose_name_plural = 'Recorridos Interactivos'

    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='RecorridoInteractivos')

    def __str__(self):
        return self.Nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Imagen.path)
        if img.width > RESOLUCION_W or img.height > RESOLUCION_H:
            output_size = (RESOLUCION_W, RESOLUCION_H)
            img.thumbnail(output_size)
            img.save(self.Imagen.path)

class ImagenesRecorrido_Interactivo(models.Model):
    class Meta:
        verbose_name = 'Imágen Recorrido Interactivo'
        verbose_name_plural = 'Imágenes Recorrido Interactivo'

    Imagen = models.ImageField(upload_to='ImagenesGaleria')
    Recorrido_Interactivo = models.ForeignKey(Recorrido_Interactivo, on_delete=models.CASCADE
                               , related_name="Recorrido_Interactivo_imagenes")

    def __str__(self):
        return "Imágen Recorrido Interactivo"

from solo.models import SingletonModel
from image_uploader_widget.widgets import ImageUploaderWidget


class Galeria(models.Model):  # models.Model
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'

    Nombre = models.CharField(max_length=50)

    # @staticmethod
    # def get_instance():
    #     return Lobi.objects.get_or_create(pk=1)

    def __str__(self):
        return "Lobi"

class ImagenesGaleria(models.Model):
    class Meta:
        verbose_name = 'Imágen Galeria'
        verbose_name_plural = 'Imágenes Galeria'

    Imagen = models.ImageField(upload_to='ImagenesGaleria')
    Galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE
                               , related_name="galeria_imagenes")

    def __str__(self):
        return "Imágen Galeria"

class Vitrina(models.Model):
    class Meta:
        verbose_name = 'Vitrina'
        verbose_name_plural = 'Vitrinas'

    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='Vitrinas')
    Recorrido_Interactivo = models.ForeignKey(Recorrido_Interactivo, on_delete=models.CASCADE
                                              , related_name="Recorrido_Interactivo_Vitrina")

    def __str__(self):
        return self.Nombre

# class Articulo_Vitrina(models.Model):
#     class Meta:
#         verbose_name = 'Articulo Vitrina'
#         verbose_name_plural = 'Articulos Vitrina'
#
#     Nombre = models.CharField(max_length=50)
#     Descripcion = models.TextField()
#     Imagen = models.ImageField(upload_to='Articulo_Objeto')
#     Vitrina = models.ForeignKey(Vitrina, on_delete=models.CASCADE
#                                               , related_name="Vitrina_Articulo_Vitrina")
#
#     def __str__(self):
#         return self.Nombre

class Articulo_Independiente(models.Model):
    class Meta:
        verbose_name = 'Articulo Independiente'
        verbose_name_plural = 'Articulos Independiente'

    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='Articulo_Objeto')


    def __str__(self):
        return self.Nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Imagen.path)
        if img.width > RESOLUCION_W or img.height > RESOLUCION_H:
            output_size = (RESOLUCION_W, RESOLUCION_H)
            img.thumbnail(output_size)
            img.save(self.Imagen.path)


class RecorridoVirtual(models.Model):
    class Meta:
        verbose_name = 'Recorrido Virtual'
        verbose_name_plural = 'Recorridos Virtuales'

    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Video = models.FileField(upload_to='recorrido_virtual')


    def __str__(self):
        return self.Nombre