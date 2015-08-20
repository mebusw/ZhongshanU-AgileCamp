# -*-coding:utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from OnlineExchange.models import User, Product
from Constant.constant import *
import datetime
from random import randint
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
    if 'username' in request.COOKIES:
        # user has logged in
        username = request.COOKIES['username']
        users = User.objects.all()
        for user in users:
            if user.tel == username or user.mail == username:
                uname = user.uname
                break
    else:
        username = ""
        uname = ""
    TYPE = request.GET.get("category", "0")
    if TYPE == '0':
        products = Product.objects.all()
        print "type is ", type(products[0].type)
    else:
        products = [product for product in Product.objects.all() if product.type.encode('utf8') == TYPE]
    count = 1
    productsInOneRow = []
    totalProducts = []
    for product in products:
        if len(product.description) > 40:
            product.description = product.description[:40] + '...'
        if len(product.pname) > 13:
            product.pname = product.pname[:13] + '...'
        productsInOneRow.append(product)
        if count % 3 == 0:
            totalProducts.append(productsInOneRow)
            productsInOneRow = []
        count += 1
    #resp = HttpResponse(render(request, 'dashboard.html', {'username': username, 'uname': uname}))
    #resp.delete_cookie('username', path='')
    #return render(request, 'dashboard.html', {'username': username, 'uname': uname})
    return render(request, 'dashboard.html', {'username': username, 'uname': uname, 'products': totalProducts, 'category': TYPE})


def login(request):
    """
    user login interface
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
    uname = request.GET.get('uname', None)
    tel = request.GET.get('tel', None)
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)
    if uname and tel and email and password:
        # all the parameters are not None
        users = User.objects.all()
        uids = []
        for user in users:
            if user.tel == tel:
                return HttpResponse(json.dumps(TEL_DUPLICATE), content_type="application/json")
            if user.mail == email:
                return HttpResponse(json.dumps(MAIL_DUPLICATE), content_type="application/json")
            uids.append(user.uid)
        newuid = randint(1, 10000000)
        # random int between 1-10000000
        while newuid in uids:
            newuid = randint(1, 10000000)
        newuser = User(uname=uname, uid=newuid, tel=tel, mail=email, password=password)
        newuser.save()
        response = HttpResponse(json.dumps(SUCCESS), content_type="application/json")
        dt = datetime.datetime.now() + datetime.timedelta(hours=1)
        response.set_cookie('username', tel, expires=dt)
        return response
    else:
        return HttpResponse(json.dumps(PARA_ERROR), content_type="application/json")


def getCategory(request):
    """
    user search interface, search key is product type
    """
    category = request.GET.get('type', '')
    if category == '':
        # query content is empty
        return HttpResponseRedirect('/dashboard')

    products = Product.objects.get(type=category)

    productDir = {}
    productDir['products'] = products
    response = HttpResponse(json.dumps(productDir), content_type="application/json")
    return response


def getMyProduct(request):
    """
    user search interface, scan the products of current user
    """
    uid = request.GET.get('uid', None)

    if uid:
        products = Product.objects.GET.get('uid' == uid)
        productDir = {}
        productDir['products'] = products
        response = HttpResponse(json.dumps(productDir), content_type="application/json")
        return response

    else:
        response = HttpResponse(status=403)
        return response


def homepage(request):
    """
    user interface to home page
    """
    pass


