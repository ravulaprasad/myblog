from django.urls import path
from . import views

urlpatterns=[

	path('',views.index,name='index'),
	path('Home/',views.Home,name='Home'),
	path('MVT/',views.MVT,name='MVT'),
	path('Signup/',views.Signup,name='Signup'),
	path('Login/',views.Login,name='Login'),
]