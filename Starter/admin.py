# Superuser Credentials
# User: admin
# Pass: testing123
# 127.0.0.1:8000/admin

from django.contrib import admin

from .models import Person, Steam

admin.site.register(Person)
admin.site.register(Steam)