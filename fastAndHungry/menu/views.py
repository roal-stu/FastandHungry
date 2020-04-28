from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View


# Models
from .models import Element,Category

# Create your views here.

class ElementMixin(object):
    title = 'Page title'
    
    def get_context_data(self, **kwargs):
        
        # Call class's get_context_data method to retrieve context
        context = super().get_context_data(**kwargs) 
        
        context['title'] = self.title
        return context

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

class ElementCreate(ElementMixin,CreateView):
    """Create Element.
    TODO: Add  new element
    """
    model = Element
    fields = '__all__'
    title = 'Crear Platillo'

class ElementUpdate(ElementMixin,UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    model = Element
    fields = '__all__'
    title = 'Editar Platillo'

class ElementDelete(DeleteView):
    model = Element
    success_url = '/'

