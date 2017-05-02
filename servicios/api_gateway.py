# coding=utf-8

'''
Este archivo contiene una simulación de la función del API Gateway que
en el diagrama está contenido en el TYK, pero que para esta tarea no se
implementará como tal.
'''

import os
import requests
from flask import request
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/api/tweet/search", methods=['GET'])
def obtener_tweets():
    url = 'http://localhost:8084/api/tweet/search'
    response = requests.get(url, request.args)
    return response.json(), response.status_code


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8085))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
