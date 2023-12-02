from django.shortcuts import render
from .api_service import get_api

def sitelist_details(request):
    # Chiamata all'API esterna che restuisce il json con i dati di tutti i Site
    api_data = get_api(endpoint='sitelist',id="")
    
    if api_data is not None:
        # Passa i dati al template
        context = {'site': api_data}
        print(context)
        return render(request, 'site_list.html', context)
    else:
        # Gestisci il caso in cui la chiamata all'API non sia riuscita
        return render(request, 'errore_template.html')
