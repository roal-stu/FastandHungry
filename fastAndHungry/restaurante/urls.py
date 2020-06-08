"""Restaurante URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Views
from restaurante import views

app_name = "restaurante"
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('menu/', views.Menu.as_view(), name='menu'),

	path('elements-admin/', views.Elements.as_view(), name = 'elements_admin'),
	path('update-element/<int:pk>/', views.ElementUpdate.as_view(), name="element_edit"),
	path('delete-element/<int:pk>/', views.ElementDelete.as_view(), name="element_delete"),
	path('create-element/', views.ElementCreate.as_view(), name="element_create"),

	path('categorys-admin/', views.Categorys.as_view(), name = 'categorys_admin'),
	path('update_category/<int:pk>/', views.CategoryUpdate.as_view(), name="category_edit"),
	path('delete_category/<int:pk>/', views.CategoryDelete.as_view(), name="category_delete"),
	path('create_category/', views.CategoryCreate.as_view(), name="category_create"),
	
] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

