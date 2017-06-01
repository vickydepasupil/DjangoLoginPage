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

class RegistrationForm(forms.ModelForm):
	email = forms.EmailField(label="Email")
	email2 = forms.EmailField(label="Confirm")
	password  = forms.CharField(label='Password', widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username','email','email2','password']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")

		if email != email2:
			raise forms.ValidationError("E-mails must be the same.")

		email_check = User.objects.filter(email=email)
		if email_check.exists():
			raise forms.ValidationError("E-mail has already been registered.")

		return email

