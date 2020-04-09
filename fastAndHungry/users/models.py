from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtendedUser(models.Model): 
	user = models.OneToOneField(
		User, related_name="extended_user", on_delete=models.CASCADE
	)
