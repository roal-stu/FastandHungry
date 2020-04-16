from django.shortcuts import render
from django.views import View

# Models
from .models import Element,Category

# Create your views here.

class ElementView(View):
    """Top songs.
    TODO: Show songs by its popularity.
    """

    template = "menu/element.html"

    def get(self, request):
        """GET method."""

        element_id = request.GET.get()
        element = Element.objects.filter(id = element_id)

        context = {"element":element}

        return render(request, self.template, context)
