from django.apps import AppConfig

# Ensures Django loads the signal when the app starts


class PlanningAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "planning_app"

    def ready(self):
        import planning_app.signals
