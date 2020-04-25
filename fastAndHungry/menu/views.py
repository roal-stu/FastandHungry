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


class ElementUpdate(UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    model = Element
    fields = '__all__'
    """template = "menu/add_element.html"

    def get(self, request, id):
        GET method.
        title = 'Editar platillo'
        element = get_object_or_404(Element, id=id)
        form = ElementForm(initial={'name': element.name, 'price': element.price, 
                                    'description': element.description, 'image': element.image } )
        context = {"form": form, "title" : title}
        return render(request, self.template, context)
    
    def post(self, request, id):
        Receive and validate sign up form.
        element = get_object_or_404(Element, id=id)
        form = ElementForm(request.POST, request.FILES)
        context = {}
        if not form.is_valid():
            title = 'Editar platillo'
            context = {"form": form, "title" : title}
            return render(request, self.template, context)

        element.name = form.cleaned_data.get("name") 
        element.price = form.cleaned_data.get("price")
        element.description = form.cleaned_data.get("description")
        element.img = form.cleaned_data.get("image") 
        element.save() 
        return redirect("/")"""
