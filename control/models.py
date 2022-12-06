from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Warehouse(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    space = models.IntegerField(validators=[MinValueValidator(0)])
    occupied_space = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.user.email}: {self.space}"

    # def save(self, *args, **kwargs):
    #     if self.occupied_space > self.space:
    #         self.occupied_space = self.space
    #     return super().save(*args, **kwargs)

    def fill(self, amount):
        self.occupied_space += amount

    def get_free_space(self):
        return self.space - self.occupied_space


class Purchase(models.Model):

    warehouse = models.ForeignKey(Warehouse, related_name="purchases", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    cost = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.title[:15]}... {self.date}"


class Shipment(models.Model):

    warehouse = models.ForeignKey(Warehouse, related_name="shipments", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=255)
    cost = models.FloatField(validators=[MinValueValidator(0.01)])
    delivery_cost = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.title[:15]}... {self.date}"


class PurchaseArchive(models.Model):

    user = models.ForeignKey(User, related_name="archive_purchases", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    cost = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.title[:15]}... {self.date}"


class ShipmentArchive(models.Model):

    user = models.ForeignKey(User, related_name="archive_shipments", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=255)
    cost = models.FloatField(validators=[MinValueValidator(0.01)])
    delivery_cost = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.title[:15]}... {self.date}"