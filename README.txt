1) CREARE LE VARIABILI DI AMBIENTE
	API_ENVIROMENT: dev, prod
2) ISTALLARE LE DIPENDENZE
	pip install -r requirements.txt
3) API ENDPOINT
    correggere il file /config/config.json con gli endpoint corretti
4) MIGRAZIONE DATABASE
    rm db.sqlite3 #solo la prima volta
    python manage.py migrate