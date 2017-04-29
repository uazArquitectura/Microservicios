import commands
import json


def analizar_tweet(txt):
    # Comando que usara la API de text-processing para analizar el tweet
    cmd = 'curl -d "text=' + txt + '" http://text-processing.com/api/sentiment/'
    # Se ejecuta el comando
    output = commands.getoutput(cmd)
    # Verifica si hubo error en la conexion con la API
    if output.find('Could not resolve host') != -1: return 'ERROR'
    # Encuentra el indice donde comienza el json con la respuesta
    index_json = output.find('{')
    # Extrae la subcadena con el json de la respuesta
    json_str = output[index_json:]
    # Interpreta el json como objeto de python
    response = json.loads(json_str)
    # Devuelve el sentimiento obtenido
    return response['label']


print analizar_tweet('hello world')
