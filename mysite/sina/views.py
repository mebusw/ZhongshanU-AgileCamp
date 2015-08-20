from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    usr = request.POST.get('username','noname')
    pwd = request.POST.get('password','' )
    return render(request,'sina/index.html',{'usr':usr,'pwd':pwd})

<<<<<<< HEAD
# http://120.0.0.1/sina
def index ( request ):
	pla = request.POST.get('place' , '')

	# add to placename
	Placename.objects.create(name = pla)
	place_list = Placename.objects.all()

	name_list = []
	for i in place_list:
		name_list.append(i.name)

	maxplace_name = ''
	max_counter = 0 
	for i in name_list:
		if max_counter < name_list.count(i) :
			max_counter = name_list.count(i)
			maxplace_name = i   

	
	return render(request, 'sina/index.html' ,
		{ 'pla':pla	, 'list':name_list[2:] , 'maybe_place' :maxplace_name } ) 
=======
def zzmap(request):
	return render(request,'sina/zzmap.html',{})
	
def help(request):
	return render(request,'sina/help.html',{})

def homepage(request):
	return render(request,'sina/index.html',{})
	
def record(request):
	return render(request,'sina/record.html',{})
>>>>>>> 6a9738ede68a1c8f4ed6aaf4cb3fe17a469250ec
