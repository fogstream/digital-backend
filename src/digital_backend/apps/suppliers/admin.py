from django.contrib import admin

from digital_backend.apps.suppliers.models import (
    Supplier, SupplierType, Tender, TenderMember,
    Vote)


@admin.register(SupplierType)
class SupplierTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ...


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    ...


class TenderMemberInline(admin.StackedInline):
    model = TenderMember


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = (TenderMemberInline, )
