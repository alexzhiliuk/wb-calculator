from django.test import TestCase
from django.contrib.auth.models import User
from control.models import Warehouse


class WarehouseTest(TestCase):

    def setUp(self):
        self.u = User.objects.create(
            username="test",
            email="test@mail.ru",
            password="1"
        )
        self.w = Warehouse.objects.create(user=self.u, space=10, occupied_space=0)

    def test_warehouse_free_space(self):
        """Check free space of the warehouse after filling"""
        self.w.fill(6)
        self.assertEqual(self.w.get_free_space(), 4)