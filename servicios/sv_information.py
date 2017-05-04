# coding=utf-8
# !/usr/bin/env python

# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_information.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Abril 2017
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es porporcionar en un objeto JSON
#   información detallada acerca de una pelicula o una serie en particular haciendo uso del API proporcionada
#   por IMDb ('https://www.imdb.com/').
#
#
#
#                                        sv_information.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON que  | - Utiliza el API de    |
#           |    Procesador de      |    contenga información |   IMDb.                |
#           |     comentarios       |    detallada de pelí-   | - Devuelve un JSON con |
#           |       de IMDb         |    culas o series en    |   datos de la serie o  |
#           |                       |    particular.          |   pelicula en cuestión.|
#           +-----------------------+-------------------------+------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8084/api/v1/information?t=matrix
#
import os
import requests
from flask import Flask, abort, request
from flask.ext.api import FlaskAPI, status

app = FlaskAPI(__name__)


@app.route("/information")
def get_information():
    if 'titulo' in request.args.keys():
        titulo = request.args['titulo']
        url = 'http://www.omdbapi.com/?t=' + titulo + '&plot=full&r=json'
        response_omdb = requests.get(url, request.args)
        return response_omdb.json(), response_omdb.status_code
    else:
        error_response = {'message': 'Parámetros incompletos'}
        return error_response, status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'Servicio sv_information'
    print '--------------------------------------------------------------------'
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8087))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda
    # acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
