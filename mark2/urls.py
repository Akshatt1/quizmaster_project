from django.contrib import admin
from django.urls import path
from mark2 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete,name='delete')
]


