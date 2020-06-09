from django.contrib import admin

#Models
from .models import *

# Register your models here.

admin.site.register(Element)
admin.site.register(Category)
admin.site.register(OrderElement)
admin.site.register(Order)