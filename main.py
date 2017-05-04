# coding=utf-8
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Tarea 2 - Arquitectura de Microservicios
--------------------------------------------------------------------------------
Archivo: main.py
Autor: Porfirio Ángel Díaz Sánchez
--------------------------------------------------------------------------------
Descripción general:
Este script levanta los servicios y demás elementos necesarios para el
funcionamiento del sistema.
--------------------------------------------------------------------------------
'''

import os
import webbrowser


# Método que corre un programa de python abriendo una nueva terminal.
def run_python_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"python " + program_name + "\"'")


# Se levantan los microservicios.
print 'Levantando el microservicio sv_gestor_tweets.py'
run_python_program('servicios/sv_gestor_tweets.py')
print 'Levantando el microservicio sv_analizador_tweets.py'
run_python_program('servicios/sv_analizador_tweets.py')
print 'Levantando el microservicio sv_information.py'
run_python_program('servicios/sv_information.py')

# Se levanta el API Gateway.
print 'Levantando el api_gateway.py'
run_python_program('api_gateway.py')

# Se levanta la GUI.
print 'Levantando el gui.py'
run_python_program('gui.py')

# Se acabó la inicialización del sistema
print 'Los componentes necesarios fueron levantados'

webbrowser.open('http://localhost:8088', new=0)
