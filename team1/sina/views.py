from django.shortcuts import render
from django.http import HttpResponse
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
		return render(request, 'sina/signin.html')
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
	if(u._usr==usr and u._pwd == pwd):
		#<script> 
		#	alert("内弄是“欢迎进入本站”之类的 "); 
		#</script>
		return render(request, 'sina/index_good.html',{'msg':'Hello '+ u._usr})
	else:
		return render(request, 'sina/fail.html')

def ask(request):
	question = request.POST.get('question','')
	q = Question.objects.create(_question = question)
	return render(request, 'sina/ask.html')

def getinfo(request):
	toWhere = request.POST.get('q1','')
	when = request.POST.get('q2','')
	peopleAmount = request.POST.get('q3','')
	fromWhere = request.POST.get('q4','')
	budget = request.POST.get('q5','')
	otherRequest = request.POST.get('q6','')
	guide = Guide.objects.create(_toWhere = toWhere,_when = when
		_peopleAmount = peopleAmount , _fromWhere = fromWhere,
		_budget = budget , _otherRequest = otherRequest)

	return render(request,'sina/getinfo.html')