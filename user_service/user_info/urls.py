from .import views
from django.urls import path

urlpatterns = [
    path('userinfo/', views.user_info)
]