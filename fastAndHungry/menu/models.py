from django.db import models

# Create your models here.

class Category(models.Model):
    """Category Model."""

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=280)

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
       """Get str representation."""
       return self.__str__()

def element_image_directory_path(instance,filename):
    """Get element image directory path to save."""
    return f"menu/element/images/{instance.id}_{instance.name}"

class Element(models.Model):
    """Element Model."""

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=280)
    image = models.ImageField(upload_to=element_image_directory_path,null=True)

    #relatiionship
    category = models.ForeignKey(Category,models.CASCADE)

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()