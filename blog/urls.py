from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_autor/', views.add_autor, name='add_autor'),
    path('add_categoria/', views.add_categoria, name='add_categoria'),
    path('add_post/', views.add_post, name='add_post'),
]
