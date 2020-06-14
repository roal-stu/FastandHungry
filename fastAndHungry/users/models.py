from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser):
    """User Model.
    TODO: extends the django user model
    """
    is_admin = models.BooleanField(default=False)
    is_delivery_man = models.BooleanField(default=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        """Get str representation."""
        if self.first_name:
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return self.username 

    def __repr__(self):
       """Get str representation."""
       return self.__str__()

    class Meta:
        db_table = 'auth_user'


class Address(models.Model):
    """User Address.
    TODO: represents an address
    Each address must be related to a user
    """
    calle = models.CharField(max_length = 100)
    exterior = models.CharField(max_length = 100)
    interior = models.CharField(max_length = 100, null= True, blank=True)
    colonia = models.CharField(max_length = 100)
    codigo_postal = models.CharField(max_length = 100)
    delegacion = models.CharField(max_length = 100)
    entre_calle_1 = models.CharField(max_length = 100, null = True, blank=True)
    entre_calle_2 = models.CharField(max_length = 100, null = True, blank=True)
    referencias = models.CharField(max_length = 200, null = True, blank=True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE, related_name='addresses')

    def __str__(self):
        """Get str representation."""
        return 'Usuario: %s. Dirección: Calle %s, Interior %s' % (self.usuario,self.calle,self.exterior)

    def str_rep(self):
        """Get str representation."""
        if self.interior:
            return 'Calle %s, Exterior %s, Interior %s Colonia %s Delegación %s C.P. %s ' % (self.calle, self.exterior, self.interior, self.colonia, self.delegacion, self.codigo_postal)
        else:
            return 'Calle %s, Exterior %s, Colonia %s Delegación %s C.P. %s ' % (self.calle, self.exterior, self.colonia, self.delegacion, self.codigo_postal)

    def __repr__(self):
        """Get str representation."""
        return self.__str__()