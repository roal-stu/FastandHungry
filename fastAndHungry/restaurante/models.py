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
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,null=True,on_delete=models.SET_NULL)


class OrderElement(models.Model):
    """Represents a element with a quantity.
    TODO: represents a element inside a order
    """
    element = models.ForeignKey(Element,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_subtotal(self):
        return self.quantity * self.element.price

    def __str__(self):
        return self.quantity 