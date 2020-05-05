from django.contrib import admin
from django.urls import include, path

# Views
from users import views

app_name = "users"
urlpatterns = [
    path('register/',views.registerPage, name="register"),
	path('login/',views.logPage, name="login"),
	path('home/', views.home, name="home"),
    path('direc/', views.direc, name = "direc"),
    path('logout/', views.logoutUser, name="logout"),
    path('homeadmin/', views.homeAdmin, name="homeAdmin"),
    path('profile/user-edit/', views.edituser, name="user-edit"),
    path('profile/',views.view_profile, name = "profile"),
    path('update_dir/<str:pk>/', views.updateDir, name="update_dir"),
    path('delete_dir/<str:pk>/', views.deleteDir, name="delete_dir"),
    path('ver_dirs/', views.address, name="ver_dirs"),
]