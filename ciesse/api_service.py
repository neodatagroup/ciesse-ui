
# api_service.py
import requests
from django.http import JsonResponse
import json
from django.conf import settings
import os

from decouple import config

def load_env():
    config_path = os.path.join(settings.BASE_DIR, '.env')
    #config.read_file(open(config_path))

def load_config():
    config_path = os.path.join(settings.BASE_DIR, 'ciesse/config/config.json')
    
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Errore: Il file '{config_path}' non è stato trovato.")
        # Esegui azioni alternative o solleva un'altra eccezione se necessario.

def get_api(endpoint,id):
    # URL dell'API esterna
    if(id != ""):
        api_url = endpoint+str(id)
    else:
        api_url = endpoint
    
    #load_env()

    # Recupera il valore della variabile di ambiente
    #environment = config('ENVIRONMENT') + '_' + endpoint
    environment = os.environ.get("API_ENVIROMENT") +'_'+ endpoint
    #environment = 'dev_' + endpoint
    print(environment)

    load_config()
    config = load_config()
    #print(config)

    api_url = config[environment]['api_url']+str(id)
    api_key = config[environment]['api_key']
    print(api_url)
    print(api_key)
    # Insert here parameters
    params = {"api_key": api_key}#{"api_key": "H7IMR3NAX6YH490N2KSXRAPB9MBKN1QX"}

    try:
        # Effettua la richiesta GET all'API esterna
        #response = requests.get(api_url, params=params)
        print("ciao")
        response = requests.get(api_url)
        print(f"sono la risposta: {response}")
        print("addio")
        # Controlla se la richiesta ha avuto successo (status code 200)
        if response.status_code == 200:
            # Ottieni i dati JSON dalla risposta
            data = response.json()
            #print(f"sono la risposta: {data}")
            # Puoi ora elaborare i dati come desideri, ad esempio, restituire il JSON come risposta
            return data
        else:
            # Se la richiesta non ha avuto successo, restituisci un messaggio di errore
            return {'error': 'Errore nella richiesta all\'API esterna'}
    except Exception as e:
        # Gestisci eventuali eccezioni durante la richiesta
        return {'error': str(e)}