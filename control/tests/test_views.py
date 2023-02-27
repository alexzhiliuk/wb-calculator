from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User
from control.models import Warehouse, Purchase
from control.business.warehouse import get_warehouse
from datetime import date


class PurchasesTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()
        self.client.login(username="testuser", password="12345")

        self.list_url = reverse('purchases')
        self.add_url = reverse('add_purchase')

    def test_purhchase_list_GET(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'control/purchases.html')

    def test_change_warehouse_space_POST(self):

        self.client.get(self.list_url)
        response = self.client.post(self.list_url, {
            "space": 10
        })
        warehouse = Warehouse.objects.get(id=1)

        self.assertEqual(warehouse.space, 10)
        self.assertEquals(response.status_code, 302)

    def test_get_warehouse_by_user(self):

        w = Warehouse.objects.create(user=self.user, space=10, occupied_space=0)
        self.assertEqual(get_warehouse(self.user), w)
    
    def test_add_purchase_GET(self):
        
        response = self.client.get(self.add_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'control/add_purchase.html')

    def test_add_purchase_POST(self):
        
        w = Warehouse.objects.create(user=self.user, space=10, occupied_space=0)

        response = self.client.post(self.add_url, {
            "title": "Test product",
            "date": date(2023, 4, 12),
            "amount": 5,
            "cost": 2.5,
        })
        
        self.assertEqual(w.purchases.first(), Purchase.objects.first())
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.add_url, {
            "title": "Test product 2",
            "date": date(2023, 4, 13),
            "amount": 6,
            "cost": 2.5,
        })

        self.assertEqual(response.url, self.add_url)
