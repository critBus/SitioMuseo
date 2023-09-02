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


class Trabajo_Investigativo(models.Model):
    class Meta:
        verbose_name = 'Trabajo Investigativo'
        verbose_name_plural = 'Trabajos Investigativos'
    Nombre = models.CharField(max_length=50)
    Descripcion=models.TextField()
    Imagen = models.ImageField(upload_to="Trabajos Investigativos")#upload_to=APP_CNF.getRutaCarpetaImg()

    def __str__(self):
        return self.Nombre



class Articulo(models.Model):
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
    Nombre = models.CharField(max_length=50)
    Descripcion=models.TextField()
    Imagen = models.ImageField(upload_to="articulos")
    def __str__(self):
        return self.Nombre