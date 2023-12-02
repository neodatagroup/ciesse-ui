# views.py
import requests
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .api_service import get_api
from django.shortcuts import redirect

class SiteListView(View):
    def get(self, request, *args, **kwargs):
        # Chiamata all'API esterna che restuisce il json con i dati di tutti i Site
        url=""
        api_key=""
        api_data = get_api(url,api_key)
        api_data=[
            {"siteId":11, "potenza":"13", "forecast":"14.5", "indice":"basso"},
            {"siteId":12, "potenza":"3", "forecast":"13.5", "indice":"basso"},
            {"siteId":13, "potenza":"13", "forecast":"12.5", "indice":"normale"},
            {"siteId":14, "potenza":"9", "forecast":"10.5", "indice":"normale"},
            {"siteId":15, "potenza":"2", "forecast":"9", "indice":"basso"},
            {"siteId":16, "potenza":"11", "forecast":"11", "indice":"normale"},
            {"siteId":17, "potenza":"14", "forecast":"14", "indice":"normale"},
            {"siteId":18, "potenza":"14", "forecast":"13.5", "indice":"normale"}
        ]

        if api_data is not None:
            # Passa i dati al template
            context = {'site': api_data}
            print(context)
            return render(request, 'site_list.html', context)
        else:
            # Gestisci il caso in cui la chiamata all'API non sia riuscita
            return render(request, 'errore_template.html')

class ExternalApiView(View):
    def get(self, request, *args, **kwargs):
        # URL dell'API esterna
        api_url = "https://monitoringapi.solaredge.com/site/17943/inventory"
        # Insert here parameters
        params = {"api_key": "H7IMR3NAX6YH490N2KSXRAPB9MBKN1QX"}

        try:
            # Effettua la richiesta GET all'API esterna
            response = requests.get(api_url, params=params)

            # Controlla se la richiesta ha avuto successo (status code 200)
            if response.status_code == 200:
                # Ottieni i dati JSON dalla risposta
                data = response.json()

                # Puoi ora elaborare i dati come desideri, ad esempio, restituire il JSON come risposta
                return JsonResponse(data)
            else:
                # Se la richiesta non ha avuto successo, restituisci un messaggio di errore
                return JsonResponse({'error': 'Errore nella richiesta all\'API esterna'}, status=500)
        except Exception as e:
            # Gestisci eventuali eccezioni durante la richiesta
            return JsonResponse({'error': str(e)}, status=500)
