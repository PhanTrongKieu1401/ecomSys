from .import views
from django.urls import path

urlpatterns = [
    path('createbook', views.create_book),
    path('getbook', views.get_book),
    path('deletebook', views.delete_book),
    # path('addtocart', views.add_to_cart),
]
