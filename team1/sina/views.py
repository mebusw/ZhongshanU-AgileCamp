from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.
#http://127.0.0.1:8000/sina/
from sina.models import User,Question,Guide
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
	u = User.objects.get(_usr=usr)
	if(usr ==''):
		return render(request, 'sina/signin.html')
	elif(u._usr==usr and u._pwd == pwd):
		#<script> 
		#</script>
		return render(request, 'sina/index.html',{'msg':'Hello '+ u._usr})
	else:
		return render(request, 'sina/fail.html')

def ask(request):
	# question = request.POST.get('question','')
	# q = Question.objects.create(_question = question)
	# if request.method == 'POST':
		# uf=UserForm(request.POST)
	page = request.GET.get('page','')
	if(page==''):
		return render(request, 'sina/ask.html')
	else:
		url = 'sina/Ques'+page+'.html'
		return render(request, url)
def more(request):
	return render(request, 'sina/more.html')

def getinfo(request):
# 	toWhere = request.POST.get('q1','')
# 	when = request.POST.get('q2','')
# 	peopleAmount = request.POST.get('q3','')
# 	fromWhere = request.POST.get('q4','')
# 	budget = request.POST.get('q5','')
# 	otherRequest = request.POST.get('q6','')
# 	guide = Guide.objects.create(_toWhere = toWhere,_when = when
# 		_peopleAmount = peopleAmount , _fromWhere = fromWhere,
# 		_budget = budget , _otherRequest = otherRequest)
	return render(request,'sina/get_info.html')

def profile(request):
	toWhere = request.POST.get('q1','')
	when = request.POST.get('q2','')
	peopleAmount = request.POST.get('q3','')
	fromWhere = request.POST.get('q4','')
	budget = request.POST.get('q5','')
	otherRequest = request.POST.get('q6','')
	guide = Guide.objects.create(_toWhere = toWhere , _when = when,
		_peopleAmount = peopleAmount , _fromWhere = fromWhere ,
		_budget = budget , _otherRequest = otherRequest)

	return render(request,'sina/profile.html',
		{'toWhere' : guide._toWhere, 'when' : guide._when , 
		 'peopleAmount' : guide._peopleAmount , 'fromWhere' : guide._fromWhere,
		 'budget' : guide._budget , 'otherRequest' : guide._otherRequest})

def moreread(request):
	return render(request,'sina/more-read.html')

def daoyou(request):
	return render(request, 'sina/daoyou.html')