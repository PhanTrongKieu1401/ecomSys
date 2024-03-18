from .import views
from django.urls import path

urlpatterns = [
    path('userlogin/', views.user_login)
]