from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('editar/', views.editar, name='editar'),
    path('obtenerlista/', views.obtenerlista, name='obtenerlista'),
]