from django.shortcuts import render,  get_object_or_404, redirect
from django.views import View

# Models
from .models import Element,Category

#Forms
from .forms import ElementForm

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

class CreateElementView(View):
    """Create new artist
    """
    template = "menu/add_element.html"

    def get(self, request):
        """GET method."""
        form = ElementForm()
        title = 'Agregar platillo'
        context = {"form": form, "title" : title}
        return render(request, self.template, context)
    
    def post(self, request):
        """Receive and validate sign up form."""
        form = ElementForm(request.POST, request.FILES)
        context = {}
        if not form.is_valid():
            title = 'Agregar platillo'
            context = {"form": form, "title" : title}
            return render(request, self.template, context)

        name = form.cleaned_data.get("name") 
        price = form.cleaned_data.get("price")
        description = form.cleaned_data.get("description")
        img = form.cleaned_data.get("image") 
        obj = Element.objects.create( 
                             name = name,
                             price = price,
                             description = description,  
                             image = img 
                                 ) 
        obj.save() 
        return redirect("/")

class EditElementView(View):
    """Create new artist
    """
    template = "menu/add_element.html"

    def get(self, request, id):
        """GET method."""
        title = 'Editar platillo'
        element = get_object_or_404(Element, id=id)
        form = ElementForm(initial={'name': element.name, 'price': element.price, 
                                    'description': element.description, 'image': element.image } )
        context = {"form": form, "title" : title}
        return render(request, self.template, context)
    
    def post(self, request, id):
        """Receive and validate sign up form."""
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
        return redirect("/")

