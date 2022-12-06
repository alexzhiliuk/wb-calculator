from django.urls import path

from . import views

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchases'),
    path('purchase/add/', views.AddPurchaseView.as_view(), name='add_purchase'),
    path('purchase/edit/<int:uid>/', views.EditPurchaseView.as_view(), name='edit_purchase'),
    path('purchase/delete/<int:uid>/', views.delete_purchase, name='delete_purchase'),
    path('purchase/complete/<int:uid>/', views.add_purchase_to_archive, name='complete_purchase'),
    path('purchase/csv/', views.get_csv_purchases, name='csv_purchases'),
    
    path('shipments/', views.ShipmentListView.as_view(), name='shipments'),
    path('shipment/add/', views.AddShipmentView.as_view(), name='add_shipment'),
    path('shipment/edit/<int:uid>/', views.EditShipmentView.as_view(), name='edit_shipment'),
    path('shipment/delete/<int:uid>/', views.delete_shipment, name='delete_shipment'),
    path('shipment/complete/<int:uid>/', views.add_shipment_to_archive, name='complete_shipment'),
    path('shipment/csv/', views.get_csv_shipments, name='csv_shipments'),

    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('archive/delete/<str:status>/<int:uid>/', views.DeleteArchiveView.as_view(), name='delete_archive'),


]