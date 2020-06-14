from django.db import models

from django.utils.translation import gettext_lazy as _

from users.models import *
from .validators import *

# Create your models here.


def element_image_directory_path(instance,filename):
    """Get element image directory path to save."""
    return f"menu/element/images/{instance.pk}_{instance.name}"


class Category(models.Model):
    """Category Model.
    TODO: represents a category
    """
    name = models.CharField(max_length=200, verbose_name='nombre')
    description = models.CharField(max_length=280, verbose_name='descripción')
    image = models.ImageField(upload_to=element_image_directory_path, null=True, blank=True, verbose_name='imagen')

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
       """Get str representation."""
       return self.__str__()


class Element(models.Model):
    """Element Model.
    TODO: represents a element.
    Each element must be related to a category
    """
    name = models.CharField(max_length=200,verbose_name='nombre')
    price = models.IntegerField(verbose_name='precio')
    description = models.CharField(max_length=280,verbose_name='descripción')
    image = models.ImageField(upload_to=element_image_directory_path, null=True, blank=True,verbose_name='imagen')

    #relatiionship
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='categoria')

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()


class Order(models.Model):
    """Order Model.
    TODO: represents an order.
    """
    ORDER_STATES = [
        ('CT','Carrito'),
        ('PD','Pendiente'),
        ('LT','Lista'),
        ('EC','En Camino'),
        ('ET','Entregado'),
    ]

    state = models.CharField(choices=ORDER_STATES,max_length=2,verbose_name='estado')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders',verbose_name='cliente')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='approved_orders',null=True,blank=True,validators=[IsAdminValidator()])
    delivery_man = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivered_orders',null=True,blank=True,validators=[IsDeliveryManValidator()],verbose_name='repartidor')
    address = models.ForeignKey(Address,null=True,on_delete=models.SET_NULL,verbose_name='dirección')

    def full_clean(self, exclude=None, validate_unique=True):
        super().full_clean(exclude, validate_unique)
        if self.address:
            if not self.address in self.customer.addresses.all():
                raise ValidationError(
                    _('La dirección no pertenece al cliente. Usuario esperado: %(user)s, Usuario recibido: %(ad_user)s'),
                    params={ 'user' : self.customer , 'ad_user' : self.address.usuario},
            )



    def add_element(self, new_element, quantity):
        element, is_new = self.order_elems.get_or_create(element = new_element)
        if is_new:
            element.quantity = quantity
        else:
            element.quantity += quantity
        element.save()

    def is_empty(self):
        return self.order_elems.count() == 0

    def get_total(self):
        total = 0
        for elem in self.order_elems.all():
            total += elem.get_subtotal()
        return total
           
    def __str__(self):
        """Get str representation."""
        return 'Orden de %s. %s' % (self.customer.username, self.state)

    def __repr__(self):
       """Get str representation."""
       return self.__str__()


class OrderElement(models.Model):
    """Represents a element with a quantity.
    TODO: represents a element inside a order
    """
    element = models.ForeignKey(Element,on_delete=models.CASCADE,verbose_name='platillo')
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_elems',verbose_name='pedido')
    quantity = models.IntegerField(default = 1,verbose_name='cantidad')

    def get_subtotal(self):
        return self.quantity * self.element.price

    def __str__(self):
        """Get str representation."""
        return '%s.- Elemento de la orden %s. Cont: %i %s' % (self.id, self.order, self.quantity, self.element.name)

    def __repr__(self):
       """Get str representation."""
       return self.__str__()