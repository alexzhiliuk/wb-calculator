from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from control.models import *
from .forms import *
from .business.warehouse import get_warehouse
from django.contrib import messages
import csv
from django.http import HttpResponse


class PurchaseListView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = user.warehouse
        form = WarehouseForm(instance=warehouse, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse("purchases"))

    def get(self, request, *args, **kwargs):

        user = request.user
        warehouse = get_warehouse(user)
        purchases = warehouse.purchases.all()
        if request.GET.get("search"):
            purchases = purchases.filter(title__in=request.GET["search"])

        
        form = WarehouseForm(instance=warehouse)

        return render(
            request,
            "control/purchases.html",
            {
                "warehouse": warehouse,
                "purchases": purchases,
                "form": form,
            }
        )
       

class AddPurchaseView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = get_warehouse(user)
        form = PurchaseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd.get("amount") <= warehouse.get_free_space():
                new_purchase = form.save(commit=False)
                new_purchase.warehouse = warehouse
                new_purchase.save()
                
                return redirect(reverse("purchases"))
            
            messages.info(request, "Не хватает места на складе")

        return redirect(reverse("add_purchase"))


    def get(self, request, *args, **kwargs):

        form = PurchaseForm()

        return render(
            request,
            "control/add_purchase.html",
            {
                "form": form,
            }
        )
       

class EditPurchaseView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = get_warehouse(user)
        if Purchase.objects.filter(id=kwargs["uid"], warehouse=warehouse).exists():
            purchase = Purchase.objects.get(id=kwargs["uid"])
            old_amount = purchase.amount
            form = PurchaseForm(instance=purchase, data=request.POST)
        else:
            return redirect(reverse("purchases"))

        if form.is_valid():
            cd = form.cleaned_data

            # вычитаем старое значение
            warehouse.fill(-old_amount)
            warehouse.save()

            if cd.get("amount") <= warehouse.get_free_space():
                new_purchase = form.save(commit=False)
                new_purchase.save()
                
                return redirect(reverse("purchases"))

            warehouse.fill(old_amount)
            warehouse.save()
            
            messages.info(request, "Не хватает места на складе")

        return redirect(reverse("edit_purchase", kwargs={'uid':kwargs["uid"]}))


    def get(self, request, *args, **kwargs):

        user = request.user
        warehouse = get_warehouse(user)

        if Purchase.objects.filter(id=kwargs["uid"], warehouse=warehouse).exists():
            form = PurchaseForm(instance=Purchase.objects.get(id=kwargs["uid"]))
        else:
            return redirect(reverse("purchases"))

        return render(
            request,
            "control/edit_purchase.html",
            {
                "form": form,
            }
        )


def delete_purchase(request, uid):

    user = request.user
    warehouse = get_warehouse(user)
    try:
        purchase = Purchase.objects.get(id=uid)
    except:
        return redirect(reverse("purchases"))

    if purchase.warehouse == warehouse:
        purchase.delete()

    return redirect(reverse("purchases"))


def add_purchase_to_archive(request, uid):
    user = request.user
    warehouse = get_warehouse(user)
    try:
        purchase = Purchase.objects.get(id=uid)
    except:
        return redirect(reverse("purchases"))

    if purchase.warehouse == warehouse:
        PurchaseArchive.objects.create(
            user=user,
            title=purchase.title,
            date=purchase.date,
            amount=purchase.amount,
            cost=purchase.cost
            )
        purchase.delete()

    return redirect(reverse("purchases"))


def get_csv_purchases(request):

    user = request.user
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="purchases.csv"'},
    )
    writer = csv.writer(response)
    purchases = Purchase.objects.filter(warehouse=get_warehouse(user)).all().values_list("id", "title", "date", "amount", "cost")
    writer.writerow(["id", "title", "date", "amount", "cost"])
    for purchase in purchases:
        writer.writerow(purchase)
    return response


class ShipmentListView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = user.warehouse
        form = WarehouseForm(instance=warehouse, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse("shipments"))

    def get(self, request, *args, **kwargs):

        user = request.user
        warehouse = get_warehouse(user)
        shipments = warehouse.shipments.all()
        if request.GET.get("search"):
            shipments = shipments.filter(title__in=request.GET["search"])
        
        form = WarehouseForm(instance=warehouse)

        return render(
            request,
            "control/shipments.html",
            {
                "warehouse": warehouse,
                "shipments": shipments,
                "form": form,
            }
        )
       

class AddShipmentView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = get_warehouse(user)
        form = ShipmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if warehouse.occupied_space >= cd.get("amount"):
                new_shipment = form.save(commit=False)
                new_shipment.warehouse = warehouse
                new_shipment.save()
            
                return redirect(reverse("shipments"))

            messages.info(request, "Не хватает товара")            

        return redirect(reverse("add_shipment"))


    def get(self, request, *args, **kwargs):

        form = ShipmentForm()

        return render(
            request,
            "control/add_shipment.html",
            {
                "form": form,
            }
        )
       

class EditShipmentView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        warehouse = get_warehouse(user)
        if Shipment.objects.filter(id=kwargs["uid"], warehouse=warehouse).exists():
            shipment = Shipment.objects.get(id=kwargs["uid"])
            old_amount = shipment.amount
            form = ShipmentForm(instance=shipment, data=request.POST)
        else:
            return redirect(reverse("shipments"))

        if form.is_valid():
            cd = form.cleaned_data

            # Добавляем старое значение
            warehouse.fill(old_amount)
            warehouse.save()

            if warehouse.occupied_space >= cd.get("amount"):
                new_shipment = form.save(commit=False)
                new_shipment.save()
                
                return redirect(reverse("shipments"))

            warehouse.fill(-old_amount)
            warehouse.save()
            
            messages.info(request, "Не хватает товара")

        return redirect(reverse("edit_shipment", kwargs={'uid':kwargs["uid"]}))


    def get(self, request, *args, **kwargs):

        user = request.user
        warehouse = get_warehouse(user)

        if Shipment.objects.filter(id=kwargs["uid"], warehouse=warehouse).exists():
            form = ShipmentForm(instance=Shipment.objects.get(id=kwargs["uid"]))
        else:
            return redirect(reverse("shipments"))

        return render(
            request,
            "control/edit_shipment.html",
            {
                "form": form,
            }
        )


def delete_shipment(request, uid):

    user = request.user
    warehouse = get_warehouse(user)
    try:
        shipment = Shipment.objects.get(id=uid)
    except:
        return redirect(reverse("shipments"))

    if shipment.warehouse == warehouse:
        shipment.delete()

    return redirect(reverse("shipments"))


def add_shipment_to_archive(request, uid):
    user = request.user
    warehouse = get_warehouse(user)
    try:
        shipment = Shipment.objects.get(id=uid)
    except:
        return redirect(reverse("shipments"))

    if shipment.warehouse == warehouse:
        ShipmentArchive.objects.create(
            user=user,
            title=shipment.title,
            date=shipment.date,
            amount=shipment.amount,
            address=shipment.address,
            cost=shipment.cost,
            delivery_cost=shipment.delivery_cost,
            )
        shipment.delete()

    return redirect(reverse("shipments"))


def get_csv_shipments(request):

    user = request.user
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="shipments.csv"'},
    )
    writer = csv.writer(response)
    shipments = Shipment.objects.filter(warehouse=get_warehouse(user)).all().values_list(
        "id", "title", "date", "amount", "address", "cost", "delivery_cost"
        )
    writer.writerow(["id", "title", "date", "amount", "address", "cost", "delivery_cost"])
    for shipment in shipments:
        writer.writerow(shipment)
    return response


class ArchiveView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):


        user=request.user
        purchases = PurchaseArchive.objects.all().filter(user=user)
        shipments = ShipmentArchive.objects.all().filter(user=user)
        if request.GET.get("search"):
            shipments = shipments.filter(title__in=request.GET["search"])
            purchases = purchases.filter(title__in=request.GET["search"])
        items = list(purchases.values()) + list(shipments.values())
        items.sort(key=lambda x: x["id"])

        return render(
            request,
            "control/archive.html",
            {
                "items": items,
            }
        )


class DeleteArchiveView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user = request.user

        if kwargs["status"] == "purchase":
            try:
                purchase = PurchaseArchive.objects.get(id=kwargs["uid"])
            except:
                return redirect(reverse("archive"))

            if purchase.user == user:
                purchase.delete()

        if kwargs["status"] == "shipment":
            try:
                shipment = ShipmentArchive.objects.get(id=kwargs["uid"])
            except:
                return redirect(reverse("archive"))

            if shipment.user == user:
                purchase.delete()

        return redirect(reverse("archive"))
