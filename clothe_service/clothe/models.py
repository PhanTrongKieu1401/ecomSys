# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class clothe(models.Model):
    # The following are the fields of our table.
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)

    # It will help to print the values.

    def __str__(self):
        return '%s %s %s' % (
            self.name, self.price, self.product_type
        )
