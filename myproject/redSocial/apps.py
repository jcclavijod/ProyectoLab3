from django.apps import AppConfig


class RedSocialConfig(AppConfig):
    name = 'redSocial'

    def ready(self):
        import redSocial.signals
