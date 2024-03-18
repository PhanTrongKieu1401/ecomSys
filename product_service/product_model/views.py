# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import product_details

# get product


@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}

    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    # prodata = [1, 2, 3]
    for tbl_value in prodata.values():
        data.append(tbl_value)

    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

# create product


def post_product(
        product_id, product_category,
        product_name, availability, price
):
    product_data = product_details(
        product_id=product_id, product_category=product_category,
        product_name=product_name, availability=availability, price=price
    )
    product_data.save()
    return True


@csrf_exempt
def create_product(request):
    data = json.loads(request.body)
    product_id = data.get("id")
    product_category = data.get("category")
    product_name = data.get("name")
    availability = data.get("availability")
    price = data.get("price")

    resp = {}
    res = post_product(
        product_id, product_category,
        product_name, availability, price
    )
    if res:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Product is ready to dispatch.'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed !!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')

# delete product


def del_product(id):
    product_data = product_details.objects.filter(id=id)
    product_data.delete()
    return True


@csrf_exempt
def delete_product(request):
    data = json.loads(request.body)
    id = data.get("id")
    resp = {}
    res = del_product(id)
    if res:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Product is ready to dispatch.'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed !!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def get_all_product(req):
    url_book = 'http://127.0.0.1:8601/getbook'
    url_clothe = 'http://127.0.0.1:8602/getclothe'
   
    data = {}
    data['status'] = 'Success'
    data['status_code'] = '200'
    data['message'] = ''

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url_book, headers=headers)
    api_resp1 = json.loads(response.content.decode('utf-8'))

    response = requests.post(url_clothe, headers=headers)
    api_resp2 = json.loads(response.content.decode('utf-8'))

    
    data['data'] = {
        "book": api_resp1['data'],
        "clothe": api_resp2['data'],
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
