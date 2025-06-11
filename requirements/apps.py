from django.apps import AppConfig

class RequirementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requirements'

    def ready(self):
        import requirements.translation
