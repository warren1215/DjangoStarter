# Superuser Credentials
# User: admin
# Pass: testing123
# 127.0.0.1:8000/admin

from django.contrib import admin

from .models import Person, Steam, Season, PubgStat

admin.site.register(Person)
admin.site.register(Steam)
admin.site.register(Season)
admin.site.register(PubgStat)
