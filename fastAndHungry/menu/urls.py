"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from menu import views

app_name = "menu"

urlpatterns = [
    # Class-based views
    path('platillo/<int:id>/', views.ElementView.as_view(), name='see-element'),
    path('editar-platillo/<int:pk>/',views.ElementUpdate.as_view(), name = 'update-element'),
    path('crear-platillo/',views.ElementCreate.as_view(), name = 'create-element')
]