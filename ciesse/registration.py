# ciesse/registration.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Effettua il login dopo la registrazione
            return redirect('views_login')  # Sostituisci 'home' con la tua vista home
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})
