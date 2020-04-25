"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from menu import views

app_name = "menu"

urlpatterns = [
    # Class-based views
    path('platillo<int:id>', views.ElementView.as_view(), name='ver-element'),
    path('add-platillo/',views.CreateElementView.as_view(), name = 'add-element'),
    path('edit-platillo<int:id>/',views.EditElementView.as_view(), name = 'edit-element'),
]