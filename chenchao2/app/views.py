#coding=utf-8
from django.shortcuts import render
from app.models import Customer
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
# Create your views here.
def index(request):
    if  not request.REQUEST.has_key("dish") and not request.REQUEST.has_key("del"):
        tot = Customer.objects.count()
        
        num = {}
        num['A'] = Customer.objects.filter(kind='A').count()
        num['B'] = Customer.objects.filter(kind='B').count()
        num['C'] = Customer.objects.filter(kind='C').count() 
        order_num = [i[0] for i in sorted(num.iteritems(), key=lambda asd:asd[1], reverse = True)]
        print order_num
        #id = Customer.objects.last().id
        return render_to_response('app/index.html', {'tot':tot,'tot_a':num['A'],'tot_b':num['B'],'tot_c':num['C'],'dishes':'A','top1':order_num[0],'top2':order_num[1],'top3':order_num[2]})
        
    else:
        flag = True
        
        if request.REQUEST.has_key("operate"):
            kind = request.GET['dish']
            id = request.GET['id']
        elif request.REQUEST.has_key("del"):
            kind = ''
        
            id = request.GET['id']
            if id!='':
                Customer.objects.filter(id=id).delete()
            flag = False
        else:
            kind = request.GET['dish']
            person = Customer(kind=kind, num=0)
            person.save()
            id = Customer.objects.last().id
        tot = Customer.objects.count()
        num = {}
        num['A'] = Customer.objects.filter(kind='A').count()
        num['B'] = Customer.objects.filter(kind='B').count()
        num['C'] = Customer.objects.filter(kind='C').count()
        order_num = [i[0] for i in sorted(num.iteritems(), key=lambda asd:asd[1], reverse = True)]
        if flag==False:
            return render_to_response('app/index.html', {'tot':tot,'tot_a':num['A'],'tot_b':num['B'],'tot_c':num['C'],'dishes':'A','top1':order_num[0],'top2':order_num[1],'top3':order_num[2]})
        
        #print order_num
        return render_to_response('app/index.html', {'tot':tot,'tot_a':num['A'],'tot_b':num['B'],'tot_c':num['C'],'id':id,'kind':kind,'dishes':'A','top1':order_num[0],'top2':order_num[1],'top3':order_num[2]})

        
    

    
def homepage(request):
    #login(request)
    if request.REQUEST.has_key("dish"):
        kind = request.GET['dish']
        if Customer.objects.filter(kind=kind):
            Customer.objects.filter(kind=kind).first().delete()
    tot = Customer.objects.count()
    tot_a=Customer.objects.filter(kind='A').count()
    tot_b=Customer.objects.filter(kind='B').count()
    tot_c=Customer.objects.filter(kind='C').count()
    
    if Customer.objects.filter(kind='A'):
        num_a = Customer.objects.filter(kind='A').first().id
    else: 
        num_a = 0
    
    if Customer.objects.filter(kind='B'):
        num_b = Customer.objects.filter(kind='B').first().id
    else: 
        num_b = 0
    
    if Customer.objects.filter(kind='C'):
        num_c = Customer.objects.filter(kind='C').first().id
    else: 
        num_c = 0
        
    return render_to_response('app/homepage.html',{'tot':tot,'tot_a':tot_a,'tot_b':tot_b,'tot_c':tot_c,'num_a':num_a,'num_b':num_b,'num_c':num_c})

def test(request):
    dish = request.GET['dish']
    return render_to_response('app/test.html',{'dish':dish})

    
def DB(request):
    return render(request,'app/DB.html')


class UserForm(forms.Form): 
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    
    #注册
def temp(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
         #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
        #添加到数据库
            if not User.objects.filter(username__exact = username,password__exact = password):
                User.objects.create(username=username,password=password)
            response = HttpResponseRedirect('/login')
            return response
    else:
        uf = UserForm()
    return render_to_response('app/temp.html',{'uf':uf}, context_instance=RequestContext(req))
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
                response = HttpResponseRedirect('/homepage')
                #将username写入浏览器cookie,失效时间为3600
                return response
            else:
                #比较失败，还在login
                #uf['username']='密码或用户名错误'
                return render_to_response('app/login.html',{'uf':uf},context_instance=RequestContext(req))
    else:
        uf = UserForm()
    return render_to_response('app/login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def welcome(req):
    username = req.COOKIES.get('username','')
    return render_to_response('app/welcome.html' ,{'username':username})
    
def delete(req):
    id = req.GET['id']
    dish = req.GET['dish']
    return render_to_response('app/delete.html' ,{'id':id,'dish':dish},context_instance=RequestContext(req))
def temp2(req):
    return HttpResponseRedirect('login')
    id = req.GET['id']
    dish = req.GET['dish']
    #return render_to_response('app/delete.html' ,{'id':id,'dish':dish})

def deleteYes(req):
    id = req.GET['id']
    #delete from DB 
    tot = Customer.objects.count()  
    num = {}
    num['A'] = Customer.objects.filter(kind='A').count() 
    num['B'] = Customer.objects.filter(kind='B').count() 
    num['C'] = Customer.objects.filter(kind='C').count() 
    order_num = [i[0] for i in sorted(num.iteritems(), key=lambda asd:asd[1], reverse = True)]
    #return HttpResponseRedirect('index')
    return render_to_response('app/index.html', {'tot':tot,'tot_a':num['A'],'tot_b':num['B'],'tot_c':num['C'],'dishes':'A','top1':order_num[0],'top2':order_num[1],'top3':order_num[2]})
        