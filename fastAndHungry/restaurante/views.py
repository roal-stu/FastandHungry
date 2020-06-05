 # Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views import View

# Create your views here.
from .models import *
from .mixins import *



class Index(View):
    """Index.
    TODO: Show the initial page for unauthenticated user
    """
    template = "restaurante/index.html"

    def get(self, request):
        return render(request, self.template)


class Menu(LoginRequiredMixin,ListView):
    """Menu.
    TODO: Show the full menu
    """
    model = Element
    template_name = 'restaurante/menu.html'
    login_url = 'users:login'


class Elements(AdminOnlyMixin,ListView):
    """Elements.
    TODO: Show a list of all elements
    """
    login_url = 'users:login'
    model = Element
    template_name = 'restaurante/element_list.html'


class Categorys(AdminOnlyMixin,ListView):
    """Categorys.
    TODO: Show a list of all categorys
    """
    login_url = 'users:login'
    model = Category
    template_name = 'restaurante/category_list.html'


class ElementCreate(AdminOnlyMixin, CreateView):
    """Create Element.
    TODO: Add  new element
    """
    login_url = 'users:login'
    model = Element
    fields = '__all__'
    title = 'Crear Platillo'
    success_url = reverse_lazy('elements_admin')


class ElementUpdate(AdminOnlyMixin, UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    login_url = 'users:login'
    model = Element
    fields = '__all__'
    title = 'Editar Platillo'
    success_url = reverse_lazy('elements_admin')


class ElementDelete(AdminOnlyMixin, DeleteView):
    """Delete Element.
    TODO: Delete an Element
    """
    login_url = 'users:login'
    model = Element
    success_url = reverse_lazy('elements_admin')



class CategoryCreate(AdminOnlyMixin, CreateView):
    """Create Category.
    TODO: Add  new category
    """
    login_url = 'users:login'
    model = Category
    fields = '__all__'
    title = 'Crear Categoria'
    success_url = reverse_lazy('categorys_admin')


class CategoryUpdate(AdminOnlyMixin, UpdateView):
    """Update Category.
    TODO: Make changes in a Category
    """
    login_url = 'users:login'
    model = Category
    fields = '__all__'
    title = 'Editar Categoria'
    success_url = reverse_lazy('categorys_admin')



class CategoryDelete(AdminOnlyMixin, DeleteView):
    """Delete Category.
    TODO: Delete a Category
    """
    login_url = 'users:login'
    model = Category
    success_url = reverse_lazy('categorys_admin')





