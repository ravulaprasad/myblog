from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from .models import viewpost
# Create your views here.
def index(request):
	return render(request,'index.html')

def Post(request):
	viewpost1= viewpost()
	viewpost1.name= 'trying module good'
	viewpost1.desc='successfully posted from views and modules'
	viewpost1.img='mvt.png'
	return render(request,'Post.html',{'viewpost1':viewpost1})

def MVT(request):
	return render(request,'MVT.html')

def Signup(request):
	return render(request,'Signup.html')

def Login(request):
	return render(request,'Login.html')
