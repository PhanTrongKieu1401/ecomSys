# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class cart(models.Model):
    # The following are the fields of our table.

    id_product = models.IntegerField()
    product_type = models.CharField(max_length=50)
    # date_added = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField(default=1)

    # It will help to print the values.

    def __str__(self):
        return '%s %s' % (
            self.id_product, self.product_type
        )
