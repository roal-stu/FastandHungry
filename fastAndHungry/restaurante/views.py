from django.shortcuts import render
from django.views import View

# Create your views here.

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
