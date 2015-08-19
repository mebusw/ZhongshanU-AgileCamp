from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#http://127.0.0.1:8000/sina/

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
	from sina.models import User	
	usr = request.POST.get('username','')
	pwd = request.POST.get('password','')
	mail = request.POST.get('email','')
	q = User.objects.filter(_usr=usr)
	quan = q.count()
		
	if quan == 0:
		User.objects.create(_usr = usr , _pwd = pwd , _mail = mail)
		if(1):
			return render(request, 'sina/verified.html',
			{'msg': 'Hello ' + usr +', we sent a verified email to ' + mail})
	else:
		return render(request, 'sina/not_verified.html',
		{'msg': 'Hello ' + usr +', your username has been used , please try another one.'})
