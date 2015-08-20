from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def gonglv(request):
	return render(request, 'sina/gonglv.html')

def findguider(request):
	return render(request, 'sina/findguider.html')

def doguider(request):
	return render(request, 'sina/doguider.html')

def question(request):
	return render(request, 'sina/question.html')

def index(request):
	return render(request, 'sina/index.html')

	
def gonglvcontent(request):
	return render(request, 'sina/gonglvcontent.html')

def answer(request):
	return render(request, 'sina/answer.html')

	
def index(request):
    usr = request.POST.get('username', 'noname')
    pwd = request.POST.get('password','')
    #return HttpResponse('Hello World, %s, %s')
    return render(request, 'sina/index.html',{'usr':usr, 'pwd':pwd})
