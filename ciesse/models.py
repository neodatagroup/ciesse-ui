# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Puoi aggiungere campi personalizzati se necessario
    pass
