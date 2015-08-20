#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
# Create your views here.


#表单
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

#表单
class UserForm_daoyou(forms.Form): 
    name = forms.CharField(label='姓名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


def gonglv(req):
    return render(req, 'sina/gonglv.html')

def findguider(req):
    if req.method == 'POST':
        name = req.POST.get('name', 'noname')
        # uf = UserForm_daoyou(req.POST)
        # # if uf.is_valid():
        # #获得表单数据
        # name = uf.cleaned_data['name']
        # #     password = uf.cleaned_data['password']
        # #     #添加到数据库
        # #     User.objects.create(username= username,password=password)
        return HttpResponse({{ name }})
    else:
        uf = UserForm()
    return render(req, 'sina/findguider.html')

def doguider(request):
    return render(request, 'sina/doguider.html')

def question(request):
    return render(request, 'sina/question.html')

def answer(request):
    return render(request, 'sina/answer.html')

def index(request):
    return render(request, 'sina/index.html')

    
def gonglvcontent(request):
    return render(request, 'sina/gonglvcontent.html')

    
def liuyanban(request):
    return render(request, 'sina/liuyanban.html')

    
# def index(request):
#     usr = request.POST.get('username', 'noname')
#     pwd = request.POST.get('password','')
#     #return HttpResponse('Hello World, %s, %s')
#     return render(request, 'sina/index.html',{'usr':usr, 'pwd':pwd})

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('sina/regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('index')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('')
            # return HttpResponse('login success!!')
    else:
        uf = UserForm()
    return render_to_response('sina/login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('sina/index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('sina/regist.html',{'uf':uf}, context_instance=RequestContext(req))
