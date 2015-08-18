from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def begin(request):
    """
    redirect to the main page
    """
    return HttpResponseRedirect('/dashboard')

def dash(request):
    """
    return the main page
    """
    return render(request, 'dashboard.html', {})