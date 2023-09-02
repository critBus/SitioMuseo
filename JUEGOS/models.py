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


class JuegoMarcar(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # otros campos del modelo
    def porcentaje_aciertos(self):
        preguntas = Pregunta.objects.filter(juego=self)
        total_preguntas = preguntas.count()
        total_aciertos = 0
        for pregunta in preguntas:
            respuestas_correctas = pregunta.respuesta_set.filter(es_correcta=True)
            if respuestas_correctas.count() == pregunta.respuesta_set.filter(id__in=self.respuestas).count():
                total_aciertos += 1
        return (total_aciertos / total_preguntas) * 100

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    juego = models.ForeignKey(JuegoMarcar, on_delete=models.CASCADE)
    enunciado = models.TextField()
    # otros campos del modelo

    def __str__(self):
        return self.enunciado

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)
    # otros campos del modelo

    def __str__(self):
        return self.texto