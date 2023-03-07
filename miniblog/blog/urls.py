from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home,name='Homepage'),
    path('About', views.About,name='aboutpage'),
    path('Contact', views.Contact,name='Contactpage'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('sigup', views.sigup,name='sigup'),
    path('login', views.User_login,name='login'),
    path('logout', views.User_logout,name='logout'),
    path('Add_Post',views.Add_post,name='Add_post'),
    path('UpdatePost/<int:id>/',views.Update_post,name='Updatepost'),
    path('Delatepost/<int:id>/',views.delate_post,name='Delatepost'),



    



]
