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
from .forms import*
from .decorators import*


def index(request):
    template = "restaurante/index.html"
    return render(request, template)


   
@login_required(login_url='users:login')
def menu(request):
    platos = Platillo.objects.all()
    context={'platos':platos}
    return render(request, 'restaurante/menu.html',context)

	
@login_required(login_url='users:login')
@admin_only
def platillos(request):
    platos =  Platillo.objects.all()
    context = {'platos':platos}

    return render(request, 'restaurante/platillos.html', context)

@login_required(login_url='users:login')
@admin_only
def cats(request):
    cats =  Categoria.objects.all()
    context = {'cats':cats}

    return render(request, 'restaurante/cats.html', context)



@login_required(login_url='users:login')
@admin_only
def updatePlato(request, pk):

    platillo = Platillo.objects.get(id=pk)
    form = CreatePlato(instance=platillo)

    if request.method == 'POST':
        form = CreatePlato(request.POST,request.FILES, instance=platillo)
        if form.is_valid():
            form.save()
            return redirect('platillosAdmin')

    context = {'form':form}
    return render(request, 'restaurante/crearPlato.html', context)



@login_required(login_url='users:login')
@admin_only
def deletePlato(request, pk):
    platillo = Platillo.objects.get(id=pk)
    if request.method == "POST":
        platillo.delete()
        return redirect('platillosAdmin')

    context = {'platillo':platillo}
    return render(request, 'restaurante/deleteplato.html', context)



@login_required(login_url='users:login')
@admin_only
def createPlato(request):
        form = CreatePlato()
        if request.method == 'POST':
            form = CreatePlato(request.POST,request.FILES)
            if form.is_valid():
                form = form.save(commit=False)
                # dire.users = request.user
                form.save()
                return redirect('platillosAdmin')
            

        context = {'form':form}
        return render(request, 'restaurante/crearPlato.html', context)



@login_required(login_url='users:login')
@admin_only
def updateCat(request, pk):

    cat = Categoria.objects.get(id=pk)
    form = CreateCat(instance=cat)

    if request.method == 'POST':
        form = CreateCat(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cats')

    context = {'form':form}
    return render(request, 'restaurante/createCat.html', context)



@login_required(login_url='users:login')
@admin_only
def deleteCat(request, pk):
    cat = Categoria.objects.get(id=pk)
    if request.method == "POST":
        cat.delete()
        return redirect('cats')

    context = {'cat':cat}
    return render(request, 'restaurante/deleteCat.html', context)



@login_required(login_url='users:login')
@admin_only
def createCat(request):
        form = CreateCat()
        if request.method == 'POST':
            form = CreateCat(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                # dire.users = request.user
                form.save()
                return redirect('cats')
            

        context = {'form':form}
        return render(request, 'restaurante/createCat.html', context)