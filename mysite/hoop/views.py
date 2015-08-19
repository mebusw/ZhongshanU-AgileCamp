from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'hoop/index.html')

def xunwuqishi(request):
	return render(request, 'hoop/xunwulianjie.html')

def wuwujiaohuan(request):
	return render(request, 'hoop/wuwujiaohuan.html')