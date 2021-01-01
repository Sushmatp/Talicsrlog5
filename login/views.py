from django.shortcuts import render,redirect
from login import views
from django.http import HttpResponse
from rlogdata.models import *
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.template import Context
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_page(request):
	return render(request,'index_login.html')
'''def user_login(request):
	if request.method=='POST':
		UserName =request.POST.get('UserName')
		Password=request.POST.get('Password')

		check_if_user_exists = Usr_table.objects.filter(UserName="UserName").exists()

		if check_if_user_exists:
			user = authenticate(request, UserName=UserName, Password=Password)
			if user is not None:
				return redirect('/dash/')
				#return render(request,'index_login.html')

            # this user is valid, do what you want to do
        
    
            # this user is not valid, he provided wrong password, show some error message
		else:

			return render(request,'index_login.html')
			#return redirect('/dash/')

        # there is no such entry with this username in the table'''

'''def user_login(request):
	if request.method=='POST':
		username =request.POST.get('username')
		password=request.POST.get('password')
		#Usr_table.objects.get('username','password')
		x=authenticate(request, username=username, password=password)

		if x is not None:
			login(request,x)
			return redirect('/dash/')
		
	context={}
	return render(request,'index_login.html',context)'''
'''def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(UserName=username, password=password)
        print("auth",str(authenticate(UserName=username, password=password)))

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect('/dash/')
       
        else:
        	return render(request,'index_login.html')'''
      	
def user_login(request):
	if request.method=='POST':
		username1=request.POST['username']
		password1=request.POST['password']
		x=authenticate(request, UserName=username1, password=password1)

		if x is  not None:
			
			return redirect('/dash/')
		
	context={}
	return render(request,'index_login.html',context)