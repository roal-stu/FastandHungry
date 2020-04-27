from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import authenticate
from .models import*



class SignUpForm(forms.Form):
    """Sign up new user form."""

    first_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    calle = forms.CharField(max_length=100)
    numero = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length = 100)
    telefono = forms.CharField(max_length=100)
    codigoPostal = forms.CharField(max_length = 100)



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count()>0:
            raise forms.ValidationError("Este correo ya está registrado")
        return data

    def clean_user(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).count()>0:
            raise forms.ValidationError("El nombre de usuario ya existe, intente con otro")
        return data


class CreateDirecForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ["users"]
