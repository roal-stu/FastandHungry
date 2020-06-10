from django.db import models

from users.models import *

# Create your models here.


def element_image_directory_path(instance,filename):
    """Get element image directory path to save."""
    return f"menu/element/images/{instance.pk}_{instance.name}"


class Category(models.Model):
    """Category Model.
    TODO: represents a category
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=280)
    image = models.ImageField(upload_to=element_image_directory_path, null=True, blank=True)

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
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=280)
    image = models.ImageField(upload_to=element_image_directory_path, null=True, blank=True)

    #relatiionship
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

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
        ('CT','CARRITO'),
        ('PD','PENDIENTE'),
        ('LT','LISTA'),
        ('EC','EN CAMINO'),
        ('ET','ENTREGADO'),
    ]

    state = models.CharField(choices=ORDER_STATES,max_length=2)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='approved_orders',null=True)
    delivery_man = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivered_orders',null=True)
    address = models.ForeignKey(Address,null=True,on_delete=models.SET_NULL)

    def add_element(self, new_element, quantity):
        element, is_new = self.order_elems.get_or_create(element = new_element)
        if is_new:
            element.quantity = quantity
        else:
            element.quantity += quantity
        element.save()

    def is_empty(self):
        if self.order_elems:
            return False
        return True
           
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
    element = models.ForeignKey(Element,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_elems')
    quantity = models.IntegerField(default = 1)

    def get_subtotal(self):
        return self.quantity * self.element.price

    def __str__(self):
        """Get str representation."""
        return '%s.- Elemento de la orden %s. Cont: %i %s' % (self.id, self.order, self.quantity, self.element.name)

    def __repr__(self):
       """Get str representation."""
       return self.__str__()