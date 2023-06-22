from django.urls import path
from . import views as views_modulo_http

urlpatterns = [
    # URL por defecto del módulo endpoint HTTP.
    # En este caso, al ser un único endpoint, hubiera válido también con
    # añadir esta url en el archivo urls.py del proyecto.
    path("", views_modulo_http.getRespuesta, name='getRespuesta'),
]