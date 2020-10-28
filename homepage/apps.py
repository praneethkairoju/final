from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'homepage'

    def ready(self):
        pass
        # write your startup code here you can import application code here
        #from app_name.models import MyModel
