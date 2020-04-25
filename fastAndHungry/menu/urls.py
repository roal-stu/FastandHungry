"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from menu import views

app_name = "menu"

urlpatterns = [
    # Class-based views
    path('platillo/<int:id>', views.ElementView.as_view(), name='element'),
    path('crear-platillo/',views.ElementCreate.as_view(), name = 'create-element')
]