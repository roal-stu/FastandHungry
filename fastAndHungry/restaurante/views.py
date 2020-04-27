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



class Menu(View):
    """Top songs.
    TODO: Show songs by its popularity.
    """

    template = "restaurante/menu.html"

    def get(self, request):
        """GET method."""
        platillos = Platillo.objects.all()
        print(platillos)
        return render(request, self.template, {"platillos": platillos})


	
class Index(View):
    """Music index.
    Showing some artists, songs, albums and playlists.
    TODO: Show artists.
    TODO: Show songs.
    TODO: Show albums.
    TODO: Show playlists.
    """

    template = "restaurante/index.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)