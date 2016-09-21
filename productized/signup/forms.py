from django.contrib.auth.models import User

class signUpForm(forms.ModelForm):
	model = User
	fields = ('first_name', 'last_name', 'email')