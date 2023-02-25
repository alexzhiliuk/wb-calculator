from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from control.models import *
from control.api.serializers import *


class WarehouseViewset(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class PurchaseViewset(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseArchiveViewset(viewsets.ModelViewSet):
    queryset = PurchaseArchive.objects.all()
    serializer_class = PurchaseArchiveSerializer


class ShipmentViewset(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    
class ShipmentViewset(viewsets.ModelViewSet):
    queryset = ShipmentArchive.objects.all()
    serializer_class = ShipmentArchiveSerializer