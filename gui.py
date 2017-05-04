# coding=utf-8
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Tarea 2 - Arquitectura de Microservicios
--------------------------------------------------------------------------------
Archivo: gui.py
Autor: Porfirio Ángel Díaz Sánchez
--------------------------------------------------------------------------------
Descripción general:
Este archivo define la interfaz gráfica del usuario. Recibe los parámetros que
posteriormente son enviados al API Gateway para la comunicación con los
servicios que utiliza el sistema.
--------------------------------------------------------------------------------
Descripción de los elementos:
- GUI
    Responsabilidad
        - Proporcionar la interfaz gráfica con la que el usuario hará uso del
        sistema.
    Propiedades:
        - Consume el API Gateway que se comunica con los servicios que
        proporcionan información al usuario.
'''

import os
from flask import Flask, render_template, request
import json
import requests
import webbrowser

'''
--------------------------------------------------------------------------------
Definición de las rutas con las que se comunica la GUI.
--------------------------------------------------------------------------------
'''

app = Flask(__name__)


# Ruta que renderiza la pantalla principal del sistema.
@app.route("/")
def index():
    return render_template("index.html")


# Ruta que recibe el título de la serie o película que se ingresa por medio
# del template index.html, realiza el análisis correspondiente, y renderiza
# el resultado en el template status.html.
@app.route("/information", methods=['GET'])
def sentiment_analysis():
    # Solicitud al servicio sv_information, por medio del API Gateway.
    url = 'http://localhost:8085/api/movie/information'
    response_omdb = requests.get(url, request.args)
    if response_omdb.status_code == 400:
        return response_omdb.json(), response_omdb.status_code
    json_result = {}
    json_result['omdb'] = response_omdb.json()
    # Solicitud al servicio sv_gestor_tweets, por medio del API Gateway.
    url = 'http://localhost:8085/api/tweet/search'
    response_obtener = requests.get(url, request.args)
    if response_obtener.status_code == 400:
        return response_obtener.json(), response_obtener.status_code
    # Solicitud al servicio sv_analizador_tweets, por medio del API Gateway.
    url = 'http://localhost:8085/api/tweet/analizar'
    response_analizar = requests.post(url, {'tweets': json.dumps(
        response_obtener.json())})
    if response_analizar.status_code == 400:
        return response_analizar.json(), response_analizar.status_code
    json_result['twitter'] = response_analizar.json()
    # Se manda renderizar el template html con los datos que debe cargar
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
    port = int(os.environ.get('PORT', 8088))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    webbrowser.open('http://localhost:8088', new=0)
