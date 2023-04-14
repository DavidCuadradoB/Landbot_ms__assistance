from django.apps import AppConfig

from assistance import container


class AssistanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assistance'

    def ready(self):
        container.wire(modules=[".views"])
