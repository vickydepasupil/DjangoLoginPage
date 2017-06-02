#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from .models import WebUser
from .forms import LoginForm, RegistrationForm

def register_view(request):
	print(request.user.is_authenticated())
	logintoken = "logintoken"
	title = "Register"
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False);
		user.set_password(form.cleaned_data.get("password"))
		user.save()

		ser = authenticate(username="username", password="password")
		login(request, user)

		context = {
		"success_message": "Conratulations!",
		"next_line": "You are now a registered happy peanut."
		}
	
		return render(request, "login/message.html", context)

	context = {
		"form": form,
		"title":title,
		"logintoken":logintoken
	}

	return render(request, 'login/form.html', context)

def login_view(request):
	print(request.user.is_authenticated())
	title = "Login"
	register = "register"
	form = LoginForm(request.POST, request.FILES)

	if form.is_valid():
		
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())

		context = {
		"login_message": "Welcome!",
		"next_line": "Thank you for visiting this page."
		}
	
		return render(request, "login/message.html", context)
	
	return render(request, 'login/form.html', {'form':form, 'title': title, 'register':register})

def logout_view(request):
	auth.logout(request)
	return render(request, "login/form.html", {"form":form})