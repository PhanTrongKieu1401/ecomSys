from .import views
from django.urls import path

urlpatterns = [
    path('userregistration/', views.registration_req)
]