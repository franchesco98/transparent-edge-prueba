from django.urls import include, path

urlpatterns = [
    # Añadimos la URL del endpoint como la URL principal del proyecto.
    path('', include('modulo_http.urls')),
]
