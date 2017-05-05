# coding=utf-8
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Tarea 2 - Arquitectura de Microservicios
--------------------------------------------------------------------------------
Archivo: sv_analizador_tweets.py
Autor: Porfirio Ángel Díaz Sánchez
--------------------------------------------------------------------------------
Descripción general:
Este archivo define el rol de un servicio. Su función es proporcionar un JSON
con el resultado del análisis de sentimientos hecho a los tweets que se reciben
como parámetro por medio de otro JSON.
--------------------------------------------------------------------------------
Descripción de los elementos:
- Analizador de tweets
    Responsabilidad
        - Analizar los tweets y determinar su connotación.
    Propiedades:
        - Utiliza la API de text-processing para el análisis de texto.
        - Determina si un tweet es positivo, negativo o neutro.
'''

import commands
import json
import os
from flask import request
from flask.ext.api import FlaskAPI, status

'''
--------------------------------------------------------------------------------
Definición del microservicio
--------------------------------------------------------------------------------
'''

app = FlaskAPI(__name__)


@app.route("/api/tweet/analizar", methods=['POST'])
def analizar_tweets():
    if 'tweets' in request.form.keys():
        tweets = json.loads(request.form['tweets'])
        sentimientos = {'positivos': 0, 'negativos': 0, 'neutros': 0,
                        'totales': 0}
        for tweet in tweets:
            tweet_body = u''.join(tweet['tweet_body']).encode('utf-8')
            tweet_body = tweet_body.replace('"', '\\"')
            cmd = 'curl -d "text=' + tweet_body \
                  + '" http://text-processing.com/api/sentiment/'
            output = commands.getoutput(cmd)
            if output.find(
                    'Could not resolve host') != -1: return 'ERROR ' + cmd
            index_json = output.find('{')
            json_str = output[index_json:]
            if json_str == '':
                sentimiento = 'neutral'
            else:
                sentimiento = json.loads(json_str)['label']
            if sentimiento == 'pos':
                sentimientos['positivos'] += 1
            elif sentimiento == 'neg':
                sentimientos['negativos'] += 1
            elif sentimiento == 'neutral':
                sentimientos['neutros'] += 1
        sentimientos['totales'] = sentimientos['positivos'] + sentimientos[
            'negativos'] + sentimientos['neutros']
        return sentimientos, status.HTTP_200_OK
    else:
        error_response = {'message': 'Parámetros incompletos'}
        return error_response, status.HTTP_400_BAD_REQUEST


'''
--------------------------------------------------------------------------------
Ejecución del microservicio
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'Servicio sv_analizador_tweets'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8086))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
