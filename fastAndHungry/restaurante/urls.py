from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Views
from restaurante import views

urlpatterns = [
path('', views.index, name='index'),

] 

