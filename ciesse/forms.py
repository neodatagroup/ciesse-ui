# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from ciesse.models import CustomUser  # Assicurati di importare CustomUser dal tuo models.py

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Usa il modello utente personalizzato
        fields = ('username', 'password')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Utilizza il tuo modello utente personalizzato
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user