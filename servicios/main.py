# coding=utf-8

'''
Este script realiza el levantamiento de todos los componentes del sistema.
'''

import sv_gestor_tweets
import api_gateway
import os


def run_python_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"python " + program_name + "\"'")


# Se levantan los microservicios
print 'Levantando el microservicio sv_gestor_tweets.py'
run_python_program('sv_gestor_tweets.py')

print 'Levantando el api_gateway.py'
# Se levanta el API Gateway
run_python_program('api_gateway.py')

print 'Los componentes necesarios fueron levantados'
