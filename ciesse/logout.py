from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('views_login')  # Sostituisci 'home' con l'URL a cui desideri reindirizzare dopo il logout
