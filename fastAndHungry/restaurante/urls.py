from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Views
from restaurante import views

urlpatterns = [
path('', views.index, name='index'),
path('platillosAdmin/', views.platillos, name = 'platillosAdmin'),
path('update_plato/<int:pk>/', views.updatePlato, name="update_plato"),
path('delete_plato/<str:pk>/', views.deletePlato, name="delete_plato"),
path('create_plato/', views.createPlato, name="create_plato"),
path('menu/', views.menu, name='menu'),
path('update_cat/<int:pk>/', views.updateCat, name="update_cat"),
path('delete_cat/<str:pk>/', views.deleteCat, name="delete_cat"),
path('create_cat/', views.createCat, name="create_cat"),
path('catsAdmin/', views.cats, name = 'cats'),


] 
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

