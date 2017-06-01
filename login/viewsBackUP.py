#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import WebUser
from .forms import UserForm

def saveUser(request):
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		nameEntered = request.POST.get('username')

		counter = 0

		webuser = WebUser.objects.all()

		for user in webuser:
			if (user.username == nameEntered): 
				msg = {'error_message': "We're sorry " + nameEntered + ", but that name is taken.", 'next_line': "Try another one?" }
				counter = 1
				break
			else:
				pass

		if (counter == 1):
 			return render(request, 'login/message.html', msg)
 		else:
			if form.is_valid():
				form.save()
				msg = {'success_message':"Thank you for signing up.", 'next_line':"Have a nice day!"}
				return render(request, 'login/message.html', msg)
			else:
				msg = {'error_message':"Sorry, something went wrong.", 
					'next_line':"You're only allowed a maximum of 10 characters for your username.", 'third_line':"Try again?"}
				return render(request, 'login/message.html', msg)
	else:
		formA = UserForm()
		return render(request, 'login/registration.html', {'form': formA})


def authUser(request, *args, **kwargs):
	if request.method == 'POST':

		nameEntered = request.POST.get('username')
		passEntered = request.POST.get('password')

		counter = 0

		webuser = WebUser.objects.all()

		for user in webuser:
			if (user.username == nameEntered): 
				if (user.password == passEntered):
					webuser = {'login_message': "Welcome back, " , 'next_line': user.username + "!" }
					counter = 1
					break
				else:
					pass
			else:
				pass

		if (counter == 0):
			webuser = {'error_message': "Sorry, you are not in our system.", 'third_line': "Please create an account first, "+ nameEntered +"."}
			# webuser = {'name':nameEntered}

		return render(request, 'login/message.html', webuser)

	else:
		formA = UserForm()
		return render(request, 'login/login.html', {'form': formA})