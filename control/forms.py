from django import forms
from control.models import *


class WarehouseForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = ("space", )

    def __init__(self, *args, **kwargs):
        super(WarehouseForm, self).__init__(*args, **kwargs)

        self.fields["space"].widget.attrs.update({"min": "1", "step": "1"})


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ("title", "date", "amount", "cost")
        labels = {
            "title": "Название товара",
            "date": "Дата доставки",
            "amount": "Кол-во доставляемого товара",
            "cost": "Стоимость доставки",
        }

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["date"].widget.attrs.update({"type": "date"})
        self.fields["amount"].widget.attrs.update({"min": "1", "step": "1"})
        self.fields["cost"].widget.attrs.update({"min": "0.01", "step": "0.01"})


class ShipmentForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = ("title", "date", "address", "amount", "cost", "delivery_cost")
        labels = {
            "title": "Название товара",
            "date": "Дата доставки",
            "amount": "Кол-во товара для поставки",
            "address": "Адрес СЦ",
            "cost": "Стоимость поставки",
            "delivery_cost": "Стоимость доставки до покупателя",
        }

    def __init__(self, *args, **kwargs):
        super(ShipmentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["date"].widget.attrs.update({"type": "datetime-local"})
        self.fields["amount"].widget.attrs.update({"min": "1", "step": "1"})
        self.fields["cost"].widget.attrs.update({"min": "0.01", "step": "0.01"})
        self.fields["delivery_cost"].widget.attrs.update({"min": "0.01", "step": "0.01"})
