from django.shortcuts import render
from django.http import HttpResponse
from sina.models import Placename

# Create your views here.

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