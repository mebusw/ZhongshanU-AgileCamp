from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000/sina/
def index(request):
	usr = request.POST.get('username','noname')
	pwd = request.POST.get('password','')
	if(usr == 'noname'):
		return render(request, 'sina/index.html')
	elif(usr =='jason' and pwd == '123'):
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
	if(1):
		return render(request, 'sina/verified.html',
		{'msg': 'Hello ' + usr +', we sent a verified email to ' + mail})
