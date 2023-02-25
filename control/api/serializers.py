from rest_framework import serializers
from control.models import *


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ['id', 'user', 'space', 'occupied_space']


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['id', 'warehouse', 'title', 'date', 'amount', 'cost']


class PurchaseArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseArchive
        fields = ['id', 'user', 'title', 'date', 'amount', 'cost']


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = ['id', 'warehouse', 'title', 'date', 'amount', 'address', 'cost', 'delivery_cost']


class ShipmentArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShipmentArchive
        fields = ['id', 'user', 'title', 'date', 'amount', 'address', 'cost', 'delivery_cost']
