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
	path('menu/category/<int:pk>/', views.CategoryView.as_view(), name='category'),

	path('elements-admin/', views.Elements.as_view(), name = 'elements_admin'),
	path('update-element/<int:pk>/', views.ElementUpdate.as_view(), name="element_edit"),
	path('delete-element/<int:pk>/', views.ElementDelete.as_view(), name="element_delete"),
	path('create-element/', views.ElementCreate.as_view(), name="element_create"),

	path('categorys-admin/', views.Categorys.as_view(), name = 'categorys_admin'),
	path('update-category/<int:pk>/', views.CategoryUpdate.as_view(), name="category_edit"),
	path('delete-category/<int:pk>/', views.CategoryDelete.as_view(), name="category_delete"),
	path('create-category/', views.CategoryCreate.as_view(), name="category_create"),

	path('add-to-cart/<int:pk>/', views.AddToCart.as_view(), name='add_to_cart'),
	path('cart/', views.CartView.as_view(), name='cart'),
	path('delete-cart-element/<int:pk>/', views.DeleteFromCart.as_view(), name='element_cart_delete'),

	path('mark-order-delivered/<int:pk>', views.MarkOrderDelivered.as_view(), name='mark_order_delivered'),
	
] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

