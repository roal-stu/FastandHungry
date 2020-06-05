from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser):
	"""User Model.
    TODO: extends the django user model
    """
	is_customer = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_delivery_man = models.BooleanField(default=False)
	
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

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
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)