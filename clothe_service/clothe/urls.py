from .import views
from django.urls import  path

urlpatterns = [
    path('createclothe', views.create_clothe),
    path('getclothe', views.get_clothe), 
    path('deleteclothe', views.delete_clothe),

]
