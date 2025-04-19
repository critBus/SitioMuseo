from django.core.management.base import BaseCommand
from django.apps import apps
import json
from django.db import models

class Command(BaseCommand):
    help = 'Importa datos desde un archivo JSON a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Ruta al archivo JSON con los datos')

    def deserialize_field(self, field, value, model_cache):
        """Deserializa un campo específico"""
        if value is None:
            return None
        
        if isinstance(field, (models.ForeignKey, models.OneToOneField)):
            if value is None:
                return None
            related_model = field.remote_field.model
            return related_model.objects.get(id=value)
        elif isinstance(field, models.ManyToManyField):
            if not value:
                return []
            related_model = field.remote_field.model
            return [related_model.objects.get(id=v) for v in value]
        elif isinstance(field, (models.DateTimeField, models.DateField, models.TimeField)):
            from django.utils.dateparse import parse_datetime, parse_date, parse_time
            if isinstance(field, models.DateTimeField):
                return parse_datetime(value) if value else None
            elif isinstance(field, models.DateField):
                return parse_date(value) if value else None
            else:
                return parse_time(value) if value else None
        else:
            return value

    def handle(self, *args, **options):
        file_path = options['file']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'No se encontró el archivo {file_path}'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('El archivo no tiene un formato JSON válido'))
            return

        # Importar datos para cada modelo
        for model_name, serialized_data in data.items():
            try:
                app_label, model_name = model_name.split('.')
                model = apps.get_model(app_label, model_name)
                
                self.stdout.write(f"Importando datos para {model_name}...")
                
                # Deserializar y guardar los datos
                for obj_data in serialized_data:
                    fields_data = obj_data['fields']
                    instance = model()
                    
                    # Primero guardamos los campos normales
                    for field in model._meta.fields:
                        if field.name in fields_data:
                            value = self.deserialize_field(field, fields_data[field.name], {})
                            setattr(instance, field.name, value)
                    
                    # Guardamos la instancia
                    instance.save()
                    
                    # Luego manejamos los campos many-to-many
                    for field in model._meta.many_to_many:
                        if field.name in fields_data:
                            value = self.deserialize_field(field, fields_data[field.name], {})
                            if value:
                                getattr(instance, field.name).set(value)
                
                self.stdout.write(self.style.SUCCESS(f'Datos importados exitosamente para {model_name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al importar datos para {model_name}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Proceso de importación completado')) 