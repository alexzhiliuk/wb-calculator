from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import *


@receiver(pre_delete, sender=Purchase)
def add_free_place(sender, instance, **kwargs):
    warehouse = instance.warehouse
    warehouse.fill(-(instance.amount))
    warehouse.save()


@receiver(pre_save, sender=Purchase)
def add_occupied_place(sender, instance, **kwargs):
    warehouse = instance.warehouse
    warehouse.fill(instance.amount)
    warehouse.save()


@receiver(pre_save, sender=Shipment)
def add_shipment(sender, instance, **kwargs):
    warehouse = instance.warehouse
    warehouse.fill(-(instance.amount))
    warehouse.save()


@receiver(pre_delete, sender=Shipment)
def delete_shipment(sender, instance, **kwargs):
    warehouse = instance.warehouse
    warehouse.fill(instance.amount)
    warehouse.save()
    
