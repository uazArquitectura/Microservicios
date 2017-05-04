# coding=utf-8
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Tarea 2 - Arquitectura de Microservicios
--------------------------------------------------------------------------------
Archivo: sv_information.py
Autor: Porfirio Ángel Díaz Sánchez
--------------------------------------------------------------------------------
Descripción general:
Este archivo define el rol de un servicio. Su función general es proporcionar
en un objeto JSON información detallada acerca de una pelicula o una serie en
particular haciendo uso del API proporcionada por IMDb (https://www.imdb.com).
--------------------------------------------------------------------------------
Descripción de los elementos:
- Procesador de comentarios de IMDb
    Responsabilidad
        - Ofrecer un JSON que contenga información detallada de películas o
        series en particular.
    Propiedades:
        - Utiliza la API de IMDb.
        - Devuelve un JSON con datos de la serie o película en cuestión.
'''
import json
import os
import requests
from flask import request
from flask.ext.api import FlaskAPI, status

app = FlaskAPI(__name__)


@app.route("/information")
def get_information():
    if 'titulo' in request.args.keys():
        titulo = request.args['titulo']
        url = 'http://www.omdbapi.com/?t=' + titulo + '&plot=full&r=json'
        response_omdb = requests.get(url, request.args)
        if 'Error' in response_omdb.json():
            error_response = {'message': response_omdb.json()['Error']}
            return error_response, status.HTTP_404_NOT_FOUND
        return response_omdb.json(), response_omdb.status_code
    else:
        error_response = {'message': 'Parámetros incompletos'}
        return  error_response, status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'Servicio sv_information'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8087))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
