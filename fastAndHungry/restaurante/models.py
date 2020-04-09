from django.db import models

class categoria(models.Model):
	name = models.CharField(max_length=100)


class platillo(models.Model):

	name = models.CharField(max_length=200)
	price = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	image = models.ImageField(upload_to = "restaurante/media/platillos/{instance.id}_{instance.name}_{filename}",null=True,blank = True)



# Create your models here.
