# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from cart.models import cart


def data_insert(id_product, product_type):
    cart_data = cart(id_product = id_product, product_type=product_type)
    cart_data.save()
    return 1

def findcart(id_product, product_type):
    book_data = cart.objects.filter(id_product=id_product, product_type=product_type)
    for value in book_data.values():
        return value

@csrf_exempt
def get_all(request):
    data = []
    resp = {}

    cart_data = cart.objects.all()

    for tbl_cart in cart_data.values():
        data.append(tbl_cart)
    
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = ''
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def add(request):
    data = json.loads(request.body)

    id_product = data.get("id_product")
    product_type = data.get("product_type")
    cart_data = findcart(id_product, product_type)
    resp = {}
    if id_product and product_type:
        if cart_data :
            resp['status'] = 'Failed'
            resp['status_code'] = '200'
            resp['message'] = 'san pham da co trong cart!'
            resp['data'] = {}

            return HttpResponse(json.dumps(resp), content_type='application/json')
        else: 
                respontdata = data_insert(id_product, product_type)
                if respontdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'san pham được them vao cart.'
                    resp['data'] = data
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Fail!!!'
                    resp['data'] = {}
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Fail!!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')
