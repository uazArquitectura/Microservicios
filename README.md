# Arquitectura de Microservicios (Repositorio de la tarea 2)

## Sistema de Procesamiento de Comentarios

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:
Flask
    Versión: 0.10.1
    Descripción: Micro framework de desarrollo
requests
    Versión: 2.12.4
    Descripción: API interna utilizada en Flask para trabajar con las peticiones hacia el servidor

*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
> sudo pip install Flask==0.10.1  
> sudo pip install requests==2.12.4

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el servicio:  
   > python micro_servicios/sv_information.py  
1. Ejecutar el GUI:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!

## Requisitos adicionales de la nueva versión del sistema

### Instalar Curl
```
sudo apt-get install curl
```

### Instalar Twython
```
pip install twython
```

### Instalar requests[security]
``` 
pip install 'requests[security]' 
```
### Instalar sqlite3
```
udo apt-get install sqlite3 libsqlite3-dev
```

### Instalar Flask-API
```
sudo pip install Flask-API
```