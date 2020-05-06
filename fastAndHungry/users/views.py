from django.shortcuts import render

 # Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import*


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
				user = form.save()
				username = form.cleaned_data.get('username')
				group = Group.objects.get(name='customer')
				user.groups.add(group)
				messages.success(request, 'Cuenta creada con exito con el usuario: ' + username)

				return redirect('users:login')
			

		context = {'form':form}
		return render(request, 'users/register.html', context)
		

@login_required(login_url='users:login')

def address(request):
	direcs =  request.user.customers.all()
	context = {'direcs':direcs}

	return render(request, 'users/direc.html', context)


@login_required(login_url='users:login')

def direc(request):
		dire = CreateDirecForm()
		if request.method == 'POST':
			dire = CreateDirecForm(request.POST,)
			if dire.is_valid():
				dire = dire.save(commit=False)
				# dire.users = request.user
				dire.save()
				dire.users.add(request.user)
				return redirect('users:ver_dirs')
			

		context = {'form':dire}
		return render(request, 'users/regis2.html', context)

@login_required(login_url='users:login')

def updateDir(request, pk):

	direc = Customer.objects.get(id=pk)
	form = CreateDirecForm(instance=direc)

	if request.method == 'POST':
		form = CreateDirecForm(request.POST, instance=direc)
		if form.is_valid():
			form.save()
			return redirect('users:ver_dirs')

	context = {'form':form}
	return render(request, 'users/regis2.html', context)


@login_required(login_url='users:login')

def deleteDir(request, pk):
	direc = Customer.objects.get(id=pk)
	if request.method == "POST":
		direc.delete()
		return redirect('users:ver_dirs')

	context = {'item':direc}
	return render(request, 'users/deleteDir.html', context)



def logPage(request):
	if request.user.is_authenticated:
		group = request.user.groups.all()[0].name
		if group == 'customer':
			return redirect('users:home')

		if group == 'admin':
			return redirect('users:homeAdmin')
		
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:

				login(request, user)
				group = None
				if request.user.groups.exists():
					group = request.user.groups.all()[0].name

				if group == 'customer':
					return redirect('users:home')

				if group == 'admin':
					return redirect('users:homeAdmin')
				
			else:
				messages.info(request, 'Usuario o contraseña incorrectos')
		context = {}
		return render(request, 'users/login.html',context)


@login_required(login_url='users:login')
def home(request):
	return render(request, 'users/home.html',{} )


@login_required(login_url='users:login')
@admin_only
def homeAdmin(request):
	return render(request, 'users/menu.html',{} )


def logoutUser(request):
	logout(request)
	return redirect('users:login')


@login_required(login_url='users:login')
def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
		args = {'user': user}
	return render(request, 'users/profile.html', args)


@login_required(login_url='users:login')
def edituser(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect(reverse('users:profile'))
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'users/user-edit.html', args)





# 	{% block body %}
# <div class="container">
#     <h1>Perfil</h1>
#     <p>Usuario: {{ user }}</p>
#     <p>Email: {{ user.email }}</p>
#     <a class="btn btn-light btn-xl" href="{% url 'users:user-edit' %}">Modificar datos</a>
# </div>
