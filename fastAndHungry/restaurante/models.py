from django.db import models

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
    category = models.ForeignKey(Category,models.CASCADE)

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()