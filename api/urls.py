from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes, name='quienes'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]