from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from OnlineExchange.models import User, Product
from Constant.constant import *
import datetime

import simplejson
import json

# Create your views here.

def begin(request):
    """
    redirect to the main page
    """
    return HttpResponseRedirect('/dashboard')


def dash(request):
    """
    return the main page
    """
    data = {}
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        record = User.objects.get(tel=username)
        uname = record.uname
    else:
        username = ""
        uname = ""
    #resp = HttpResponse(render(request, 'dashboard.html', {'username': username, 'uname': uname}))
    #resp.delete_cookie('username', path='')
    #return render(request, 'dashboard.html', {'username': username, 'uname': uname})
    return render(request, 'dashboard.html', {'username': username, 'uname': uname})


def login(request):
    """

    """
    username = request.GET.get('username', 'noname')
    password = request.GET.get('password', 'nopassword')
    Users = User.objects.all()
    FIND = False
    for user in Users:
        if (username == user.tel or username == user.mail) and password == user.password:
            FIND = True
            break
    rescode = ""
    if FIND:
        rescode = SUCCESS
        dt = datetime.datetime.now() + datetime.timedelta(hours=1)
        response = HttpResponse(json.dumps(rescode), content_type="application/json")
        response.set_cookie("username", username, expires=dt)
        #HttpResponse.set_cookie("username", username)
        # return HttpResponse(simplejson.dumps(rescode), mimetype="application/json")
    else:
        rescode = PASSWORD_ERROR
        response = HttpResponse(json.dumps(rescode), content_type="application/json")
        # return HttpResponse(simplejson.dumps(rescode), mimetype="application/json")
    return response

   # return HttpResponse(json.dumps(response_data),content_type = "application/json")


def logout(request):
    """
    user logout interface
    """
    response = HttpResponseRedirect('/dashboard')
    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    return response


def register(request):
    """
    user register interface
    """
    pass

def getCategory(request):
    '''

    '''
    category = request.GET.get('type', 0)
    products = Product.objects.get(type == category)

    productDir = {}
    productDir['products'] = products

    response = HttpResponse(json.dumps(productDir),content_type="application/json")
    return response

def getMyProduct(request):
    '''
    '''
    uid = request.GET.get('uid',None)

    if uid
        products = Product.objects.GET.get('uid' == uid)

        productDir = {}
        productDir['products'] = products

        response = HttpResponse(json.dumps(productDir),content_type="application/json")
        return response

    else
        return response = HttpResponse(status=403)
