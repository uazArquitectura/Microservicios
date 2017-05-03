# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
Este archivo contiene una simulación de la función del API Gateway que
en el diagrama está contenido en el TYK, pero que para esta tarea no se
implementará como tal.
'''

import json
import os
import requests
from flask import request
from flask.ext.api import FlaskAPI

'''
--------------------------------------------------------------------------------
Definición del API Gateway
--------------------------------------------------------------------------------
'''

app = FlaskAPI(__name__)


# Ruta que llama al microservicio sv_gestor_tweets para que busque los tweets
# acerca de la serie o película cuyo título se recibe como parámetro y
# devuelva un JSON con los resultados.
@app.route("/api/tweet/search", methods=['GET'])
def obtener_tweets():
    url = 'http://localhost:8084/api/tweet/search'
    response = requests.get(url, request.args)
    return response.json(), response.status_code


# Ruta que llama al microservicio sv_analizador_tweets para que analice los
# tweets que son recibidos como parámetro y devuelva un JSON con el análisis
# hecho.
@app.route("/api/tweet/analizar", methods=['POST'])
def analizar_tweets():
    url = 'http://localhost:8084/api/tweet/search'
    response_obtener = requests.get(url, request.form)
    if response_obtener.status_code != 400:
        response_obtener.json(), response_obtener.status_code
    url = 'http://localhost:8086/api/tweet/analizar'
    response_analizar = requests.post(url, {'tweets': json.dumps(
        response_obtener.json())})
    return response_analizar.json(), response_analizar.status_code


'''
--------------------------------------------------------------------------------
Ejecución del API Gateway
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'API Gateway'
    print '--------------------------------------------------------------------'
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8085))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda
    # acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
