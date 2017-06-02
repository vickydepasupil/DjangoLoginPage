from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=12)
 	password  = forms.CharField(label='Password', widget=forms.PasswordInput)

 	def clean(self, *args, **kwargs):
 		username = self.cleaned_data.get("username")
 		password = self.cleaned_data.get("password")

 		if username and password:
 			user = authenticate(username=username, password=password)
 			if not user:
 				raise forms.ValidationError("User does not exit")

	 		return super(LoginForm, self).clean(*args, **kwargs)

