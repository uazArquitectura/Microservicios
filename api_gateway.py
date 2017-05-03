# -*- coding: utf-8 -*-
# !/usr/bin/env python

# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Abril 2017
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe dos parámetros que posteriormente son enviados
#   a servicios que la interfaz utiliza.
#
#
#
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#

'''
Este archivo contiene una simulación de la función del API Gateway que
en el diagrama está contenido en el TYK, pero que para esta tarea no se
implementará como tal.
'''

import json
import os
import urllib

import requests
from flask import request, render_template
from flask.ext.api import FlaskAPI

'''
--------------------------------------------------------------------------------
Definición del API Gateway
--------------------------------------------------------------------------------
'''

app = FlaskAPI(__name__)


# Ruta que renderiza la pantalla principal de la aplicación
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/information", methods=['GET'])
def sentiment_analysis():
    url = 'http://localhost:8087/information'
    response_omdb = requests.get(url, request.args)
    print 'OMDB Acabado'
    if response_omdb.status_code == 400:
        return response_omdb.json(), response_omdb.status_code
    json_result = {}
    json_result['omdb'] = response_omdb.json()

    url = 'http://localhost:8084/api/tweet/search'
    response_obtener = requests.get(url, request.args)

    if response_obtener.status_code != 400:
        response_obtener.json(), response_obtener.status_code
    url = 'http://localhost:8086/api/tweet/analizar'
    response_analizar = requests.post(url, {'tweets': json.dumps(
        response_obtener.json())})



    # url = 'http://localhost:8085/api/tweet/analizar'
    # response_twitter = requests.post(url, request.args)
    json_result['twitter'] = response_analizar.json()
    print 'Twitter Acabado'

    # # Se obtienen los parámetros que nos permitirán realizar la consulta
    # title = request.args.get("t")
    # url_omdb = urllib.urlopen(
    #     "https://uaz.cloud.tyk.io/content/api/v1/information?t=" + title)
    # # Se lee la respuesta de OMDB
    # json_omdb = url_omdb.read()
    # # Se convierte en un JSON la respuesta leída
    # omdb = json.loads(json_omdb)
    # # Se llena el JSON que se enviará a la interfaz gráfica para mostrársela al usuario

    # Se regresa el template de la interfaz gráfica predefinido así como los datos que deberá cargar
    return render_template("status.html", result=json_result)


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
    # TODO Resolver problema de codificación JSON
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
