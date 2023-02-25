from django.urls import path, include
from control.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'warehouses', api_views.WarehouseViewset)
router.register(r'purchases', api_views.PurchaseViewset)
router.register(r'archive-purchases', api_views.PurchaseArchiveViewset)
router.register(r'shipments', api_views.ShipmentViewset)
router.register(r'archive-shipments', api_views.ShipmentViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]