from django.shortcuts import render
from django.views import View

# Models
from .models import Element,Category

# Create your views here.

class Element(View):
    """Top songs.
    TODO: Show songs by its popularity.
    """

    template = "menu/element.html"

    def get(self, request):
        """GET method."""

        #songs = Song.objects.all()
        #to_play_id = request.GET.get("to_play", 1)
        #songs_to_play = Song.objects.filter(id=to_play_id)
        #if songs_to_play.count() == 0:
        #    to_play = Song.objects.first()
        #else:
        #    to_play = songs_to_play.first()

        #context = {"songs": songs, "to_play": to_play}

        #element =  Element.objects.
        return render(request, self.template, context)
