from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View


# Models
from .models import Element,Category

# Create your views here.

class MenuMixin(object):
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

class ElementCreate(MenuMixin,CreateView):
    """Create Element.
    TODO: Add  new element
    """
    model = Element
    fields = '__all__'
    title = 'Crear Platillo'

class ElementUpdate(MenuMixin,UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    model = Element
    fields = '__all__'
    title = 'Editar Platillo'

class ElementDelete(DeleteView):
    model = Element
    success_url = '/'

class CategoryView(View):
    """Element.
    TODO: Show a element of the menu
    """
    template = "menu/category.html"

    def get(self, request, id):
        """GET method."""
        category = get_object_or_404(Category, id=id)
        context = {"category":category}
        return render(request, self.template, context)

class CategoryCreate(MenuMixin,CreateView):
    """Create Element.
    TODO: Add  new element
    """
    model = Category
    fields = '__all__'
    title = 'Crear Categoria'

class CategoryUpdate(MenuMixin,UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    model = Category
    fields = '__all__'
    title = 'Editar Categoria'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/'

