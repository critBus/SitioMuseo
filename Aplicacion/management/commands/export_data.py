from django.core.management.base import BaseCommand
from django.core import serializers
from django.apps import apps
import json
import traceback
from django.db import models

class Command(BaseCommand):
    help = 'Exporta todos los datos de los modelos a un archivo JSON'

    def serialize_field(self, field, value):
        """Serializa un campo específico de manera segura para JSON"""
        if value is None:
            return None
        
        if isinstance(field, (models.ForeignKey, models.OneToOneField)):
            return value.id if value else None
        elif isinstance(field, models.ManyToManyField):
            return [obj.id for obj in value.all()]
        elif isinstance(field, models.FileField):
            return str(value) if value else None
        elif isinstance(field, models.ImageField):
            return str(value) if value else None
        elif isinstance(field, models.DateTimeField):
            return value.isoformat() if value else None
        elif isinstance(field, models.DateField):
            return value.isoformat() if value else None
        elif isinstance(field, models.TimeField):
            return value.isoformat() if value else None
        else:
            return value

    def serialize_model_instance(self, instance):
        """Serializa una instancia de modelo de manera segura para JSON"""
        data = {
            'id': instance.id,
            'model': f"{instance._meta.app_label}.{instance._meta.model_name}"
        }
        
        fields_data = {}
        for field in instance._meta.fields:
            try:
                value = getattr(instance, field.name)
                fields_data[field.name] = self.serialize_field(field, value)
            except Exception as e:
                print(f"Error serializando campo {field.name}: {str(e)}")
                fields_data[field.name] = None

        data['fields'] = fields_data
        return data

    def handle(self, *args, **options):
        try:
            # Lista de modelos a excluir (usuarios, permisos, etc.)
            excluded_models = [
                'auth.User',
                'auth.Group',
                'auth.Permission',
                'contenttypes.ContentType',
                'sessions.Session',
                'admin.LogEntry',
                'TRABAJOS_INVESTIGATIVOS.trabajo_investigativo',
                'TRABAJOS_INVESTIGATIVOS.articulo'
            ]
            excluded_apps=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'TRABAJOS_INVESTIGATIVOS'
            ]

            # Obtener todos los modelos de la aplicación
            print("loading models")
            all_models = []
            for app_config in apps.get_app_configs():
                print(app_config.name)
                if app_config.name in excluded_apps:
                    continue
                for model in app_config.get_models():
                    model_name = f"{model._meta.app_label}.{model._meta.model_name}"
                    if model_name not in excluded_models:
                        all_models.append(model)
            print("models loaded")
            # Exportar datos de cada modelo
            data = {}
            for model in all_models:
                model_name = f"{model._meta.app_label}.{model._meta.model_name}"
                self.stdout.write(f"Exportando datos de {model_name}...")
                
                # Serializar los datos del modelo de manera segura
                instances = model.objects.all()
                serialized_data = [self.serialize_model_instance(instance) for instance in instances]
                data[model_name] = serialized_data

            # Guardar en archivo JSON
            output_file = 'data_export.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            self.stdout.write(self.style.SUCCESS(f'Datos exportados exitosamente a {output_file}'))
        except Exception as e:
            print(traceback.format_exc())
            self.stdout.write(self.style.ERROR(f'Error al exportar datos: {e}'))

        