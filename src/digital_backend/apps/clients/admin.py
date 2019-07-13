from django.contrib import admin

from digital_backend.apps.clients.models import ClientType, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    ...


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    ...
