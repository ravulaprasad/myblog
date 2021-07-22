from django.shortcuts import render, resolve_url
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'home.html')

def signin(request):
	return render(request,'signin.html')