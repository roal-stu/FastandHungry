"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from restaurante import views

app_name = "restaurante"

urlpatterns = [
    # Class-based views
    path('', views.Index.as_view(), name='home'),

]