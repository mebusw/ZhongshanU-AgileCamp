from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	usr = request.POST.get('username', 'noname')
	pwd = request.POST.get('password', '')
	return render(request, 'sina/index.html',
		{'usr': usr, 'pwd': pwd})

def xunwuqishi(request):
	return render(request, 'sina/xunwulianjie.html')

def wuwujiaohuan(request):
	return render(request, 'sina/wuwujiaohuan.html')
