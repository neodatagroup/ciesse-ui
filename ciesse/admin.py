from django.contrib import admin

# Register your models here.
from ciesse.models import CustomUser

admin.site.register(CustomUser)
