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
]