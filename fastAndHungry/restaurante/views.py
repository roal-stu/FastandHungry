 # Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views import View

# Create your views here.
from .models import *
from .mixins import *
from .forms import *



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
    model = Category
    template_name = 'restaurante/menu.html'
    login_url = 'users:login'


class CategoryView(LoginRequiredMixin,ListView):
    """Category.
    TODO: Show all the elements of one category of the menu
    """
    model = Element
    template_name = 'restaurante/category_menu.html'
    login_url = 'users:login'

    def get_queryset(self):
        return super().get_queryset().filter(category_id = self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        form = AddToCartForm()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context['category_name'] = Category.objects.get(id = self.kwargs.get('pk'))
        context['form'] = form
        return context


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
    success_url = reverse_lazy('restaurante:elements_admin')


class ElementUpdate(AdminOnlyMixin, UpdateView):
    """Update Element.
    TODO: Make changes in an Element
    """
    login_url = 'users:login'
    model = Element
    fields = '__all__'
    title = 'Editar Platillo'
    success_url = reverse_lazy('restaurante:elements_admin')


class ElementDelete(AdminOnlyMixin, DeleteView):
    """Delete Element.
    TODO: Delete an Element
    """
    login_url = 'users:login'
    model = Element
    success_url = reverse_lazy('restaurante:elements_admin')


class CategoryCreate(AdminOnlyMixin, CreateView):
    """Create Category.
    TODO: Add  new category
    """
    login_url = 'users:login'
    model = Category
    fields = '__all__'
    title = 'Crear Categoria'
    success_url = reverse_lazy('restaurante:categorys_admin')


class CategoryUpdate(AdminOnlyMixin, UpdateView):
    """Update Category.
    TODO: Make changes in a Category
    """
    login_url = 'users:login'
    model = Category
    fields = '__all__'
    title = 'Editar Categoria'
    success_url = reverse_lazy('restaurante:categorys_admin')


class CategoryDelete(AdminOnlyMixin, DeleteView):
    """Delete Category.
    TODO: Delete a Category
    """
    login_url = 'users:login'
    model = Category
    success_url = reverse_lazy('restaurante:categorys_admin')


class CartView(LoginRequiredMixin, ListView):
    """Cart View.
    TODO: Show all the elements of the current user cart
    """
    model = OrderElement
    template_name = 'restaurante/cart.html'
    login_url = 'users:login'

    def get_queryset(self):
        cart, is_new_cart  = Order.objects.get_or_create(user = self.request.user, state = 'CT')
        return super().get_queryset().filter(order = cart)

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(*args, **kwargs)
        return context


class AddToCart(LoginRequiredMixin, View):
    """Add To Cart.
    TODO: Lets add an element to the cart
    """
    template_name = 'restaurante/category_menu.html'
    login_url = 'users:login'

    def post(self,request,*args,**kwargs):
        """Receive and validate add to cart form."""
        form = AddToCartForm(request.POST)
        cart, is_new_cart  = Order.objects.get_or_create(user = request.user, state = 'CT')

        element = Element.objects.get(id = self.kwargs.get('pk'))
        context = {}

        if form.is_valid():    
            quantity = form.cleaned_data.get("quantity")        
            cart.add_element(element,quantity)
 
        context = {"form": form}
        pk = element.category.id
        return redirect( reverse_lazy('restaurante:category',kwargs={'pk': pk}))


class DeleteFromCart(LoginRequiredMixin,DeleteView):
    """Delete From Cart.
    TODO: Lets delete an element from the cart
    """
    login_url = 'users:login'
    model = OrderElement
    success_url = reverse_lazy('restaurante:cart')

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class OrderView(StaffOnlyMixin,DetailView):
    """Order.
    TODO: Show the order information
    """
    login_url = 'users:login'
    model = User