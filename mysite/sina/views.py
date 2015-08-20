from django.shortcuts import render
from django.http import HttpResponse
from sina.models import Placename
import datetime

# Create your views here.

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
		if max_counter < name_list.count(i) and i != '':
			max_counter = name_list.count(i)
			maxplace_name = i   

	now = datetime.datetime.now()

	return render(request, 'sina/index.html' ,
		{ 'pla':pla	, 'list':name_list[2:] , 'maybe_place' :maxplace_name, 'time': now } ) 

def zzmap(request):
	return render(request,'sina/zzmap.html')
	
def help(request):
	return render(request,'sina/help.html')

def homepage(request):
	return render(request,'sina/index.html')
	
def record(request):
	return render(request,'sina/record.html')

def pie(request):
	place_list = Placename.objects.all()
	name_list = []
	for i in place_list:
		name_list.append(i.name)

	length = len(name_list)
	firstplace_name = ''
	first_counter = 0 
	for i in name_list:
		if first_counter < name_list.count(i) and i != '' :
			first_counter = name_list.count(i)
			firstplace_name = i   

	secplace_name = ''
	sec_counter = 0 
	for i in name_list:
		if sec_counter < name_list.count(i) and i != '' and i != firstplace_name:
			sec_counter = name_list.count(i)
			secplace_name = i  	

	thiplace_name = ''
	thi_counter = 0 
	for i in name_list:
		if thi_counter < name_list.count(i) and i != '' and i != firstplace_name and i != secplace_name:
			thi_counter = name_list.count(i)
			thiplace_name = i  		

	length -= name_list.count('')
	x = 1 - (first_counter + sec_counter + thi_counter) / length 
	x = round(x , 2)


	return render(request, 'sina/pie.html' , {'first_place' : str(firstplace_name) , 'first_factor':round(first_counter / length , 2 ), 
		'sec_place' : str(secplace_name) , 'sec_factor':round(sec_counter / length, 2) ,
		'thi_place' : str(thiplace_name) , 'thi_factor':round(thi_counter / length ,2) , 'x':x} )