from django import forms

from .models import*

#Create your forms here.

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class MakeAnOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MakeAnOrderForm, self).__init__(*args, **kwargs)
        if self.request: 
            self.fields['address'].queryset = self.fields['address'].queryset.filter(usuario=self.request.user)