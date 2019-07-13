from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #zwiazane z signals.py
    def ready(self):
        import users.signals
