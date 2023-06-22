from django.http import JsonResponse, HttpResponseNotFound
import requests

def getRespuesta(request):
    try:
        # Obtenemos el dominio al que realizar la petición GET que se pasa como parámetro en la URL.
        domain = 'http://' + request.GET['dominio']
        # Hacemos la petición a este dominio, para así obtener respuesta y devolver el código HTTP obtenido
        # y el tiempo transcurrido entre la petición y la respuesta.
        # Con allow_redirects=false evitamos que el módulo requests haga una redirección automática si la petición
        # original devuelve un 301, así se muestra el código HTTP de la petición original que se realiza en este endpoint.
        response = requests.get(domain, allow_redirects=False)
    except:
        # Si hubiera algún error, bien a la hora de obtener los parámetros de la URL o al hacer la petición,
        # generamos como respuesta un mensaje HTTP con código 400 por defecto.
        return HttpResponseNotFound()
    
    # Se devuelve el resultado de la petición si todo ha salido bien.
    return JsonResponse({
        'status': response.status_code,
        'time': str(response.elapsed.total_seconds() * 1000) + 'ms'
    })
