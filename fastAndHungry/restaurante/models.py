from django.db import models


class categoria(models.Model):
	name = models.CharField(max_length=100)


def image_directory_path(instance, filename):
    """Get images directory path to save."""
    return f"media/images/{instance.id}_{instance.name}_{filename}"

class Platillo(models.Model):

	name = models.CharField(max_length=200)
	price = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	image = models.ImageField(upload_to = image_directory_path,null=True,blank = True)

	def __str__(self):
		 return f"{self.name}"+ ":  "+ f"{self.description}......"+" "+f"{self.price}"




# Create your models here.


