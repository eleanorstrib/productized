from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Prelaunch_signup(forms.ModelForm):
	class Meta: 
		model = User
		fields = ('first_name', 'last_name', 'email')
