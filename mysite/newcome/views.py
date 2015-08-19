from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    usr = request.POST.get('username','noname')
    pwd = request.POST.get('password','' )
    return render(request,'newcome/index0.html',{'usr':usr,'pwd':pwd})

def zzmap(request):
	return render(request,'newcome/zzmap.html',{})
