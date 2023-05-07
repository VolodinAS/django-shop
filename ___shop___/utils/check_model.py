from django.apps import apps


def check_model(app_label: str, model_name: str) -> bool:
    return apps.get_model(app_label, model_name) is not None
