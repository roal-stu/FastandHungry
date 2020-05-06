from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreatePlato(ModelForm):
    class Meta:
        model = Platillo
        fields = "__all__"

class CreateCat(ModelForm):
	class Meta:
		model = Categoria
		fields = "__all__"
     


