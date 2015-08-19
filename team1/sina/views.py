from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#http://127.0.0.1:8000/sina/
from sina.models import User
from django.core.exceptions import ObjectDoesNotExist
def index(request):
	from sina.models import User	
	usr = request.POST.get('username','noname')
	pwd = request.POST.get('password','')
	p = User.objects.filter(_usr=usr)
	p_quan = p.count()
	if(usr == 'noname'):
		return render(request, 'sina/index.html')
	elif(usr =='jason' and pwd == '123'):
		return render(request, 'sina/ok.html',
		{'usr':'Hello ' + usr, 'pwd':pwd})
	elif(p_quan == 1):
		return render(request, 'sina/ok.html',
		{'usr':'Hello ' + usr, 'pwd':pwd})
	else:
		return render(request, 'sina/fail.html')
def signup(request):
	return render(request, 'sina/signup.html')

def verify(request):
	usr = request.POST.get('username','')
	pwd = request.POST.get('password','')
	mail = request.POST.get('email','')
	q = User.objects.filter(_usr=usr)
	quan = q.count()
		
	if quan == 0:
		User.objects.create(_usr = usr , _pwd = pwd , _mail = mail)
		if(1):
			return render(request, 'sina/verified.html',
			{'msg': 'Hello ' + usr +', we xsent a verified email to ' + mail})
	else:
		return render(request, 'sina/not_verified.html',
		{'msg': 'Hello ' + usr +', your username has been used , please try another one.'})

def signin(request):
	usr = request.POST.get('user','')
	pwd = request.POST.get('password','')
	if(usr =='E-mail address/Username'):
		return render(request,'sina/signin.html', {'warning':'Not ok'})
	try:
		u = User.objects.get(_usr=usr)	
		if(u._usr==''):
			return render(request, 'sina/',{'msg':'Hello, Guest!'})
		elif(u._usr==usr and u._pwd == pwd):
			return render(request, 'sina/index.html',{'msg':'Hello,'+ u._usr +'!'})
		else:
			return render(request, 'sina/fail.html')
	except  ObjectDoesNotExist as e:
		return render(request, 'sina/signin.html')

def more(request):
	return render(request, 'sina/more.html')
	
def ask(request):
	return render(request, 'sina/ask.html')
	