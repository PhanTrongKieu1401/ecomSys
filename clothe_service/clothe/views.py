# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from clothe.models import clothe
# import requests


def data_insert(name, price, product_type):
    clothe_data = clothe(name=name, price=price, product_type=product_type)
    clothe_data.save()
    return 1


def del_clothe(id):
    clothe_data = clothe.objects.filter(id=id)
    if clothe_data:
        clothe_data.delete()
        return True
    return False


def findID(id_product, product_type):
    clothe_data = clothe.objects.filter(
        id=id_product, product_type=product_type)
    for value in clothe_data.values():
        return value


@csrf_exempt
def create_clothe(request):
    data = json.loads(request.body)

    name = data.get("name")
    price = data.get("price")
    product_type = data.get("type")
    resp = {}
    if name and price and product_type == 'clothe':
        respontdata = data_insert(name, price, product_type)
        if respontdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = ''
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


@csrf_exempt
def get_clothe(request):
    data = []
    resp = {}
    clothe_data = clothe.objects.all()
    for tbl_value in clothe_data.values():
        data.append(tbl_value)

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
def delete_clothe(request):
    data = json.loads(request.body)
    id = data.get("id")
    resp = {}
    res = del_clothe(id)
    if res:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'delete clothe succefuly!!!'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed !!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')

