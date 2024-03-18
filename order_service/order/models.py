from django.db import models

# Create your models here.


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    # ip_address = models.IPAddressField()
    last_updated = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=20)
