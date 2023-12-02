from django.shortcuts import render
from datetime import datetime, timedelta
from . api_service import get_api

def elabora_dati(input_data):
    # Esegui la logica di elaborazione
    dati_elaborati = []

    # Converti la data di oggi in un formato datetime
    today = datetime.now().date()
    # Calcola la data di domani
    
    tomorrow1 = today + timedelta(days=1)
    tomorrow2 = tomorrow1 + timedelta(days=1)
    tomorrow3 = tomorrow2 + timedelta(days=1)

    f_tomorrow1=tomorrow1.strftime('%Y/%m/%d')
    f_tomorrow2=tomorrow2.strftime('%Y/%m/%d')
    f_tomorrow3=tomorrow3.strftime('%Y/%m/%d')
    
    #Puntatore al precedente input
    previous_entry = None
    previous_forecast1 = 0
    previous_forecast2 = 0
    previous_forecast3 = 0
    # Itera attraverso i dati in input
    for entry in input_data:
        if previous_entry is not None:
                 previous_forecast1 = previous_entry['forecast1']
                 previous_forecast2 = previous_entry['forecast2']
                 previous_forecast3 = previous_entry['forecast3']

        print(entry['data'])
        data_convertita = datetime.strptime(entry['data'], "%Y-%m-%d").strftime("%Y/%m/%d")

        data_entry = datetime.strptime(data_convertita, '%Y/%m/%d').date()
        delta = today - data_entry
        print(f"today:{today}, data_convertita:{data_entry}, delta: {delta} ")
        
        # Se la data è tra oggi - 15 giorni e oggi + 3 giorni, elabora i dati
        if  timedelta(days=0)<=delta<=timedelta(days=15):# <= timedelta(days=3):
            print(f"AAA sono dentro if: {delta}")
            dati_elaborati.append({
                'time': data_convertita,
                'effettivo': entry['production'],
                'forecast': previous_forecast1
            })
        # Aggiorna il valore precedente per il prossimo ciclo
        previous_entry = entry

    if(previous_forecast1!=0):
        dati_elaborati.append({
                'time': f_tomorrow1,
                'effettivo': 0,
                'forecast': previous_forecast1
            })
    if(previous_forecast2!=0):
        dati_elaborati.append({
                'time': f_tomorrow2,
                'effettivo': 0,
                'forecast': previous_forecast2
            })    
    if(previous_forecast3!=0):
        dati_elaborati.append({
                'time': f_tomorrow3,
                'effettivo': 0,
                'forecast': previous_forecast3
            })    
    
    
    return dati_elaborati


def monitoring_details(request,siteId):
    print(f"Sono il site id {siteId}")
    json_api_monitoring=get_api(endpoint='monitoring',id=siteId)
    json_api_anagrafica=get_api(endpoint='anagrafica',id=siteId)

    print(f"sono in monitdetail anagrafica {json_api_anagrafica}")
    
    #context = {"dati": dati}
    #context2 = {"dati": elabora_dati(json_api_monitoring)}
    context2 = {"dati": elabora_dati(json_api_monitoring),"anagrafica":json_api_anagrafica}
    
    print(context2)
    return render(request, 'monitoring.html', context2)
