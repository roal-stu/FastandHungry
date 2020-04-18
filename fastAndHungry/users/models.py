from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	email = models.EmailField(max_length=200, null=False,help_text='Required', default = "a@gmail.com")
	telefono = models.CharField(max_length=200, null=True)
	calle = models.CharField(max_length = 200 , null = False)
	interior = models.CharField(max_length = 100, null= True)
	exterior = models.CharField(max_length = 100, null = True)
	colonia = models.CharField(max_length = 100, null = True)
	codigoPostal = models.CharField(max_length = 100, null = True)
	entreCalle = models.CharField(max_length = 100, null = True)
	ycalle = models.CharField(max_length = 100, null = True)
	referencias = models.CharField(max_length = 200, null = True)
	foto = models.ImageField(upload_to = "users/media/users/{instance.id}_{instance.name}_{filename}",null=True,blank = True)

	def __str__(self):
		return self.email
