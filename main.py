# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
Este script realiza el levantamiento de todos los componentes del sistema.
'''

import os
import webbrowser


# Método que corre un programa de python abriendo una nueva terminal y
# ejecutando ahí el comando correspondiente para correrlo.
def run_python_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"python " + program_name + "\"'")


# Se levantan los microservicios
print 'Levantando el microservicio sv_gestor_tweets.py'
run_python_program('servicios/sv_gestor_tweets.py')
print 'Levantando el microservicio sv_analizador_tweets.py'
run_python_program('servicios/sv_analizador_tweets.py')
print 'Levantando el microservicio sv_information.py'
run_python_program('servicios/sv_information.py')

print 'Levantando el api_gateway.py'
# Se levanta el API Gateway
run_python_program('api_gateway.py')

print 'Los componentes necesarios fueron levantados'

print 'Ahora se va a abrir la ruta principal de la aplicación'

webbrowser.open('http://localhost:8085', new=0)
