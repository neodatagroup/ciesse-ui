from django.contrib.auth.views import LoginView
from ciesse.forms import CustomAuthenticationForm
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        # Chiamato quando il form è valido. Effettua il login e reindirizza.
        response = super().form_valid(form)
        # Puoi sostituire 'home' con l'URL a cui desideri reindirizzare l'utente dopo il login
        return redirect('site-list')