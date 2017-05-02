# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
Documentación del microservicio
'''

import commands
import json

import os
from flask import request
from flask.ext.api import FlaskAPI, status

app = FlaskAPI(__name__)


@app.route("/api/tweet/analizar", methods=['POST'])
def analizar_tweets():
    # Se verifica que el parámetro 'tweets' venga en la request
    if 'tweets' in request.form.keys():
        # Obtiene el valor del parámetro y lo interpreta como JSON
        tweets = json.loads(request.form['tweets'])
        # Diccionario donde se guardarán los resultados del análisis
        sentimientos = {'positivos': 0, 'negativos': 0, 'neutros': 0}
        count = 1
        total = len(tweets)
        # Se recorren los tweets y se contabiliza el resultado de su análisis
        for tweet in tweets:
            tweet_body = u''.join(tweet['tweet_body']).encode('utf-8')
            print str(count) + '-----> ' + tweet_body
            sentimiento = analizar_texto(tweet_body)
            # sentimiento = 'pos'
            print 'tweet ' + str(count) + ' de ' + str(
                total) + ': ' + sentimiento
            count += 1
            if sentimiento == 'pos':
                sentimientos['positivos'] += 1
            elif sentimiento == 'neg':
                sentimientos['negativos'] += 1
            elif sentimiento == 'neutral':
                sentimientos['neutros'] += 1
        return sentimientos, status.HTTP_200_OK
    else:
        # Mensaje de error
        error_response = {'message': 'Parámetros incompletos'}
        # Devuelve el mensaje de error y el código de la solicitud
        return error_response, status.HTTP_400_BAD_REQUEST


# Realiza una petición a la API de text-processing y devuelve el sentimiento
# del texto pasado como parámetro, el cual debe estar en inglés.
def analizar_texto(texto):
    # Comando que usara la API de text-processing para analizar el tweet
    cmd = 'curl -d "text=' + texto + '" http://text-processing.com/api/sentiment/'
    # Se ejecuta el comando
    output = commands.getoutput(cmd)
    # Verifica si hubo error en la conexion con la API
    if output.find('Could not resolve host') != -1: return 'ERROR'
    # Encuentra el indice donde comienza el json con la respuesta
    index_json = output.find('{')
    # Extrae la subcadena con el json de la respuesta
    json_str = output[index_json:]
    # Evalúa que venga un JSON en la cadena extraída
    if json_str == '':
        return 'neutral'
    else:
        # Interpreta el json como objeto de python
        response = json.loads(json_str)
        # Devuelve el sentimiento obtenido
        return response['label']


if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'Servicio sv_analizador_tweets'
    print '--------------------------------------------------------------------'
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8086))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda
    # acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
