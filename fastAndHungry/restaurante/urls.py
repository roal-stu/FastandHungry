from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Views
from restaurante import views

app_name = "restaurante"

urlpatterns = [
    # Class-based views
    path('', views.Index.as_view(), name='home'),

]
