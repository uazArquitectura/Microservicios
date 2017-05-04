# Arquitectura de Microservicios (Repositorio de la tarea 2)

## Sistema de Procesamiento de Comentarios

Este es un sistema de procesamiento de comentarios para las películas y 
series de Netflix, consume la API de OMDb para la consulta de resumen, 
portada, calificación, entre otros datos. Además, se analizan los tweets 
realizados acerca destos contenidos para visualizar cuántas opiniones 
positivas y negativas la gente ha realizado en Twitter. 

## Instrucciones de instalación del sistema
 
### 1. Comandos para instalar las dependencias
```
sudo pip install Flask==0.10.1  
sudo pip install requests==2.12.4
sudo apt-get install curl
sudo pip install twython
sudo pip install 'requests[security]' 
sudo apt-get install sqlite3 libsqlite3-dev
sudo pip install Flask-API
```

### 2. Descargar el proyecto
```
git clone https://github.com/uazArquitectura/Microservicios.git
```

### 3. Correr el proyecto
```
python main.py
```
## Búsquedas de ejemplo
> 13 reasons why

> stranger things

> pretty little liars

> the forger

> gossip girl

> how to get away with murder

> orange is the new black

## Link del repositorio base
https://github.com/arqdesw-curso/Arquitectura-Micro-Servicios