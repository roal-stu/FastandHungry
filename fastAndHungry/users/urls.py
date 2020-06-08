from django.contrib import admin
from django.urls import include, path

# Views
from users import views

app_name = "users"
urlpatterns = [

    path('register/',views.Register.as_view(), name="register"),
    path('login/',views.LogIn.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),

    path('home/', views.Home.as_view(), name="home"),
    path('home-admin/', views.AdminHome.as_view(), name="home_admin"),

    path('address/', views.Addresses.as_view(), name = "address_list"),
    path('edit_address/<int:pk>/', views.AddressUpdate.as_view(), name="address_edit"),
    path('delete_address/<int:pk>/', views.AddressDelete.as_view(), name="address_delete"),
    path('create_address/', views.AddressCreate.as_view(), name="address_create"),

    path('profile/user-edit/', views.ProfileUpdate.as_view(), name="user_edit"),
    path('profile/',views.ProfileView.as_view(), name = "profile"),
    path('delete-user/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),

    path('register-delivery-man/', views.DeliveryManCreate.as_view(), name='register_delivery_man'),
    path('delivery-man-list/', views.DeliveryManList.as_view(), name='delivery_man_list'),

]