# coding=utf-8
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

import os
from flask import Flask, render_template, request
import urllib, json
import requests
import webbrowser

'''
--------------------------------------------------------------------------------
Definición de las rutas con las que se comunica la GUI.
--------------------------------------------------------------------------------
'''

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/information", methods=['GET'])
def sentiment_analysis():
    url = 'http://localhost:8085/api/movie/information'
    response_omdb = requests.get(url, request.args)
    if response_omdb.status_code == 400:
        return response_omdb.json(), response_omdb.status_code
    json_result = {}
    json_result['omdb'] = response_omdb.json()
    url = 'http://localhost:8085/api/tweet/search'
    response_obtener = requests.get(url, request.args)
    if response_obtener.status_code == 400:
        return response_obtener.json(), response_obtener.status_code
    url = 'http://localhost:8085/api/tweet/analizar'
    response_analizar = requests.post(url, {'tweets': json.dumps(
        response_obtener.json())})
    if response_analizar.status_code == 400:
        return response_analizar.json(), response_analizar.status_code
    json_result['twitter'] = response_analizar.json()
    # Se regresa el template de la interfaz gráfica predefinido así como los
    # datos que deberá cargar
    return render_template("status.html", result=json_result)


'''
--------------------------------------------------------------------------------
Ejecución del la GUI
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'GUI'
    print '--------------------------------------------------------------------'
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8088))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda
    # acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
    webbrowser.open('http://localhost:8088', new=0)
