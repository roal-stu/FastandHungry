from django.shortcuts import render,  get_object_or_404
from django.views import View

# Models
from .models import Element,Category

# Create your views here.

class ElementView(View):
    """Top songs.
    TODO: Show a eleement of the menu
    """
    template = "menu/element.html"

    def get(self, request, id):
        """GET method."""
        element = get_object_or_404(Element, id=id)
        context = {"element":element}
        return render(request, self.template, context)
