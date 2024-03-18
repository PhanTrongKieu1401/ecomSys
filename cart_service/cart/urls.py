from .import views
from django.urls import  path

urlpatterns = [
    path('getallcart', views.get_all),
    path('add', views.add),
]
