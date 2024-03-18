from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration

### This function is created for validating the user.
def user_validation(uname, password):
    user_data = user_registration.objects.filter(email = uname, password = password)
    if user_data:
        return "Valid User"
    else:
        return "Invalid User"

### This function is created for getting the user name and password.
@csrf_exempt
def user_login(request):
    uname = request.POST.get("User Name")
    password = request.POST.get("Password")
    resp = {}
    if uname and password:
        ## Calling the user_validation function for username and password validation.
        respdata = user_validation(uname, password)
        ### If a user is valid then it gives success as a response.
        if respdata == "Valid User":
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Welcome to Ecommerce website......'
        ### If a user is invalid then it give failed as a response.
        elif respdata == "Invalid User":
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid credentials.'
    ### It will call when user name or password field value is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')