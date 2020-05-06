"""Menu forms."""
# Django
from django import forms

# Models
from menu.models import Element


class ElementForm(forms.Form):
    """Create new element form."""

    name = forms.CharField(max_length=200)
    price = forms.IntegerField()
    description = forms.CharField(max_length=280)
    image = forms.ImageField()

    def clean_name(self):
        """Validate that the name doesn't exist in the database.
        
        Just validating name field.
        """
        data = self.cleaned_data["name"]
        if Element.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("This element name already exists.")
        return data

