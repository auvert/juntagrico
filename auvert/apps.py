from django.apps import AppConfig

class AuvertConfig(AppConfig):
    name = 'auvert'
    verbose_name = "Genossenschaft auVert"

    def ready(self):
        pass
