from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.views import View

# Create your views here.
from .models import *
from restaurante.mixins import *
from .forms import *


class Home(LoginRequiredMixin,View):
    """Home.
    TODO: Show the home page for a customer
    """
    template = 'users/home.html'
    login_url = 'users:login'

    def get(self, request):
        return render(request, self.template)


class AdminHome(AdminOnlyMixin,View):
    """Admin Home.
    TODO: Show the home page for a admin
    """
    template = 'users/admin.html'
    login_url = 'users:login'

    def get(self, request):
        return render(request, self.template)


class LogIn(View):
    """Log In
    TODO: Show a form to log in
    """
    template = 'users/login.html'

    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return redirect('users:home_admin')
            else : 
                return redirect('users:home')
        else:
            return render(request, self.template)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            if user.is_admin:
                return redirect('users:home_admin')

            else:
                return redirect('users:home')
                
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')
            return render(request, self.template)

    
class Logout(View):
    """LogOut.
    TODO: Log Out
    """
    def get(self, request):
        logout(request)
        return redirect('/')


class Register(View):
    """Register
    TODO: Show a form to register a new user
    """
    template = 'users/register.html'
    form = CreateUserForm()

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user : home')
        else:
            context = {'form':self.form}
            return render(request, self.template, context)

    def post(self, request):
        self.form = form = CreateUserForm(request.POST)
        if self.form.is_valid():
            user = self.form.save()
            username = self.form.cleaned_data.get('username')
            user.is_customer = True
            user.save()
            messages.success(request, 'Cuenta creada con exito con el usuario: ' + username)

            return redirect('users:login')
        else: 
            context = {'form':self.form}
            return render(request, self.template, context)


class Addresses(LoginRequiredMixin,ListView):
    """Adresses.
    TODO: Show a list of all addresses
    """
    login_url = 'users:login'
    model = Address
    template_name = 'users/address_list.html'

    def get_queryset(self):
        return Address.objects.all().filter(usuario = self.request.user)


class AddressCreate(LoginRequiredMixin, CreateView):
    """Create Address.
    TODO: Add  new address to the current user
    """
    login_url = 'users:login'
    model = Address
    form_class = AddresForm
    success_url = reverse_lazy('users:address_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()        
        return super().form_valid(form)


class AddressUpdate(LoginRequiredMixin, UpdateView):
    """Update Address.
    TODO: Make changes in an Address
    """
    login_url = 'users:login'
    model = Address
    form_class = AddresForm
    success_url = reverse_lazy('users:address_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()        
        return super().form_valid(form)


class AddressDelete(LoginRequiredMixin, DeleteView):
    """Delete Addres.
    TODO: Delete an address
    """
    login_url = 'users:login'
    model = Address
    success_url = reverse_lazy('users:address_list')


class ProfileView(LoginRequiredMixin, DetailView):
    """Profile.
    TODO: Show current user information
    """
    login_url = 'users:login'
    model = User

    def get_object(self):
        return self.request.user


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Update Profile.
    TODO: Make changes in the current user
    """
    login_url = 'users:login'
    model = User
    fields = ['first_name','last_name','email','phone_number']
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user


class DeliveryManCreate(AdminOnlyMixin, CreateView):
    """Create Delevery man.
    TODO: Add new delevery man
    """
    login_url = 'users:login'
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('users:delivery_man_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.is_delivery_man = True
        obj.save()        
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(DeliveryManCreate, self).get_context_data(*args, **kwargs)
        context['is_dm_create'] = True
        return context


class DeliveryManList(AdminOnlyMixin, ListView):
    """Delivery Man List.
    TODO: Show a list of all delivery mans
    """
    login_url = 'users:login'
    model = User
    template_name = 'users/delivery_man_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_delivery_man = True)


class UserDelete(AdminOnlyMixin, DeleteView):
    """Delete Delivery Man.
    TODO: Delete a Delivery Man
    """
    login_url = 'users:login'
    model = User
    success_url = reverse_lazy('users:delivery_man_list')