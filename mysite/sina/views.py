from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    usr = request.POST.get('username','noname')
    pwd = request.POST.get('password','' )
    return render(request,'sina/index.html',{'usr':usr,'pwd':pwd})

def zzmap(request):
	return render(request,'sina/zzmap.html',{})
	
def help(request):
	return render(request,'sina/help.html',{})

def homepage(request):
	return render(request,'sina/index.html',{})
	
def record(request):
	return render(request,'sina/record.html',{})
