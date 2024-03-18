from .import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('shipment_status/', views.shipment_status),
    path('shipment_reg_update/', views.shipment_reg_update),
]
