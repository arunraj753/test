from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return HttpResponse('This is new home')

def home2(request):
	return HttpResponse('This is new home')




def about(request):
	return HttpResponse('This is new home')

def section(request):
	return HttpResponse('This is new home')


