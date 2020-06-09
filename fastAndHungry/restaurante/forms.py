from django import forms

from .models import*

#Create your forms here.

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
