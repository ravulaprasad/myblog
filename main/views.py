from django.shortcuts import render, resolve_url
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,'index.html')

def Home(request):
	return render(request,'Home.html')

def MVT(request):
	return render(request,'MVT.html')

def Signup(request):
	return render(request,'Signup.html')

def Login(request):
	return render(request,'Login.html')