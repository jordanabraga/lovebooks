from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book(request):
	return HttpResponse("Loving books is getting even better!")
