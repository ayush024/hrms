from django import forms
from .models import User, UserProfile

class UserSignupForm(forms.ModelForm):

	password= forms.CharField(widget=forms.PasswordInput, min_length=8)
	confirm_password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta:
		model = User	
		fields = ["email", "username"]
	
	def clean(self):
		cleaned_data = super(UserSignupForm, self).clean()

		password1 = cleaned_data.get("password")
		password2 = cleaned_data.get("confirm_password")

		if password1 and password2 and password1 != password2:
			self.add_error('confirm_password', "Password does not match")
		
		return cleaned_data

class UserLoginForm(forms.Form):

	email = forms.CharField(label="Email Address", max_length=50, required = False)
	password = forms.CharField(label="Password", min_length=8, widget= forms.PasswordInput)

