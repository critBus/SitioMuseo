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



class ConfiguracionGeneral(SingletonModel):
    ImagenLogo = models.ImageField(upload_to='config')
    linkFacebook=models.CharField(max_length=255,verbose_name="Link Facebook")
    linkTwitter = models.CharField(max_length=255, verbose_name="Link Twitter")
    linkYoutube= models.CharField(max_length=255, verbose_name="Link Youtube")
    correo=models.EmailField()
    telefono=models.CharField(max_length=8)
    direccion=models.CharField(max_length=255,verbose_name="Dirección")
    horarios = models.TextField()
    servidor= models.CharField(max_length=255, verbose_name="Servidor",blank=True)



    def __str__(self):
        return "Configuración General"

    class Meta:
        verbose_name = "Configuración General"

class PaginaPrincipal(SingletonModel):
    Titulo = models.CharField(max_length=255 )
    Frase=models.CharField(max_length=255)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='paginaPrincipal')

    def __str__(self):
        return "Pagina Principal"

    class Meta:
        verbose_name = "Pagina Principal"




class MenuPrincipal(SingletonModel):
    Titulo_SalaTransitoria = models.CharField(max_length=255,verbose_name="Sala Transitoria")
    Imagen_SalaTransitoria = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Sala Transitoria")

    Titulo_DescripcionDeSalas = models.CharField(max_length=255,verbose_name="Descripción DeSalas")
    Imagen_DescripcionDeSalas = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Descripción De Salas")

    Titulo_TrabajoInvestigativo = models.CharField(max_length=255,verbose_name="Trabajo Investigativo")
    Imagen_TrabajoInvestigativo = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Trabajo Investigativo")

    Titulo_Galeria = models.CharField(max_length=255,verbose_name="Galeria")
    Imagen_Galeria = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Galeria")

    Titulo_RecorridoVirtual = models.CharField(max_length=255,verbose_name="Recorrido Virtual")
    Imagen_RecorridoVirtual = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Recorrido Virtual")

    Titulo_RecorridoInteractivo = models.CharField(max_length=255,verbose_name="Recorrido Interactivo")
    Imagen_RecorridoInteractivo = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Recorrido Interactivo")

    Titulo_JuegosInteractivo = models.CharField(max_length=255,verbose_name="Juegos Interactivo")
    Imagen_JuegosInteractivo = models.ImageField(upload_to='menuPrincipal',verbose_name="Imagen Juegos Interactivo")

    def __str__(self):
        return "Menu Principal"

    class Meta:
        verbose_name = "Menu Principal"


