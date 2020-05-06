"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from menu import views

app_name = "menu"

urlpatterns = [
    # Class-based views
    path('platillo/', views.ElementView.as_view(), name='see-elements'),
    path('crear-platillo/',views.ElementCreate.as_view(), name = 'create-element'),
    path('editar-platillo/<int:pk>/',views.ElementUpdate.as_view(), name = 'update-element'),
    path('eliminar-platillo/<int:pk>/',views.ElementDelete.as_view(), name = 'delete-element' ),

    path('categoria/<int:id>/', views.CategoryView.as_view(), name='see-category'),
    path('crear-categoria/',views.CategoryCreate.as_view(), name = 'create-category'),
    path('editar-categoria/<int:pk>/',views.CategoryUpdate.as_view(), name = 'update-category'),
    path('eliminar-categoria/<int:pk>/',views.CategoryDelete.as_view(), name = 'delete-category' ),

]