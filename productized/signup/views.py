from django.shortcuts import render, render_to_response
from .forms import Prelaunch_signup

def plsignup(request):
	form = Prelaunch_signup()
	if request.method == 'POST':
		form = Prelaunch_signup(request.POST)
		if form.is_valid():
			form.save()

	return render(request, 'signup/plsignup.html', {'form': form})


