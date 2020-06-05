from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.contrib.auth import authenticate
from .models import*

class CreateUserForm(UserCreationForm):
    """Create User Form.
    TODO: a form to create a new User.
    Verify that the email and username entered are not registered
    """
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


class AddresForm(ModelForm):
    """Address Form.
    TODO: Exclude the usuario field
    """
    class Meta:
        model = Address
        exclude = ["usuario"]