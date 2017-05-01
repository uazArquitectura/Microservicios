# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Tarea 2 - Arquitectura de Microservicios
--------------------------------------------------------------------------------
Archivo: sv_gestor_tweets.py
Autor: Porfirio Ángel Díaz Sánchez
--------------------------------------------------------------------------------
Descripción general:
Este archivo define el rol de un microservicio. Su función es
proporcionar un JSON con los comentarios recabados acerca de una película o
serie de netflix por medio de la API de Twitter.
--------------------------------------------------------------------------------
Descripción de los elementos:
- ConectorTwitter
    Responsabilidad:
    Propiedades:
- ConectorSqlite
    Responsabilidad:
    Propiedades:
'''

import os
from flask import request
from flask.ext.api import FlaskAPI, status
from BuscadorTweets import BuscadorTweets
from PersistenciaTweets import PersistenciaTweets

app = FlaskAPI(__name__)


@app.route("/api/services/sv_gestor_tweets/search", methods=['GET'])
def buscar_tweets():
    # Se verifica que el parámetro 'titulo' venga en la request
    if 'titulo' in request.args.keys():
        # Obtiene el valore del parámetro
        titulo = request.args['titulo']
        # Crea instancia del buscador de tweets
        buscador = BuscadorTweets()
        # Busca y obtiene los tweets por medio del título
        tweets = buscador.search_tweets(titulo)
        # Crea instancia del manejador de sqlite
        persistencia = PersistenciaTweets()
        # for tweet in tweets:
        #     persistencia.insert_tweet(tweet.values())
        persistencia.insert_tweets(tweet.values() for tweet in tweets)
        # devuelve un JSON con los tweets y el código de la solicitud
        return persistencia.get_tweets_by_hashtag(
            buscador.to_hashtag(titulo)), status.HTTP_200_OK
    else:
        # Mensaje de error
        error_response = {'message': 'Parámetros incompletos'}
        # Devuelve el mensaje de error y el código de la solicitud
        return error_response, status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8084))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
