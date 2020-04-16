from django.contrib import admin

# Register your models here.
# Models
from .models import Element, Category

admin.site.register(Element)
admin.site.register(Category)