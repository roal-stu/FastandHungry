from django.shortcuts import render

 # Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Cuenta creada con exito con el usuario: ' + user)

				return redirect('users:login')
			

		context = {'form':form}
		return render(request, 'users/register.html', context)
		
def direc(request):
		dire = CreateDirecForm()
		if request.method == 'POST':
			dire = CreateDirecForm(request.POST,)
			if dire.is_valid():
				dire = dire.save(commit=False)
				dire.users = request.user
				dire.save()
				return redirect('users:home')
			

		context = {'form':dire}
		return render(request, 'users/regis2.html', context)


def logPage(request):
	if request.user.is_authenticated:
		return redirect('users:home')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				return redirect('users:home')
			else:
				messages.info(request, 'Usuario o contraseña incorrectos')
		context = {}
		return render(request, 'users/login.html',context)


@login_required(login_url='users:login')
def home(request):
	return render(request, 'users/home.html',{} )

def logoutUser(request):
	logout(request)
	return redirect('users:login')





	
