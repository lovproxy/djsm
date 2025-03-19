from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request, "Cпасибо за регистрацию.")
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],
									)
			login(request, new_user)
			return redirect('profile')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
	return render(request, 'profile.html')



def logout_view(request):
	logout(request)
	return redirect('')



