from django.contrib import admin
from control.models import *


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["user", "space", "occupied_space"]
    readonly_fields = ('id',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["warehouse", "title", "date", "amount", "cost"]
    readonly_fields = ('id',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ["warehouse", "title", "date", "address", "amount", "cost", "delivery_cost"]
    readonly_fields = ('id',)


@admin.register(PurchaseArchive)
class PurchaseArchiveAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "amount", "cost"]
    readonly_fields = ('id',)


@admin.register(ShipmentArchive)
class ShipmentArchiveAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "address", "amount", "cost", "delivery_cost"]
    readonly_fields = ('id',)
