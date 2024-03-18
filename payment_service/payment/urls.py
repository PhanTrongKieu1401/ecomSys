from .import views
from django.urls import  path

urlpatterns = [
    path('initiate_payment/', views.get_payment),
    path('payment_status/', views.user_transaction_info),
]
