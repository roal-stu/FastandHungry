from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View


# Models
from .models import Element,Category

#Forms
from .forms import ElementForm

# Create your views here.

class ElementView(View):
    """Element.
    TODO: Show a element of the menu
    """
    template = "menu/element.html"

    def get(self, request, id):
        """GET method."""
        element = get_object_or_404(Element, id=id)
        context = {"element":element}
        return render(request, self.template, context)

class ElementCreate(CreateView):
    """Create Element.
    TODO: Add  new element
    """
    model = Element
    fields = '__all__'
