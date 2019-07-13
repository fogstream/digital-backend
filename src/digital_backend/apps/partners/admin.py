from django.contrib import admin

from digital_backend.apps.partners.models import PartnerType, Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    ...


@admin.register(PartnerType)
class PartnerTypeAdmin(admin.ModelAdmin):
    ...
