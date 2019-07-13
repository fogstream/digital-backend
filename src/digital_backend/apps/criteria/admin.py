from django.contrib import admin

from digital_backend.apps.criteria.models import Criterion


@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    ...
