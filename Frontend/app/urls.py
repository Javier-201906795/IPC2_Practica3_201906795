from django.urls import path
from . import views

urlpatterns = [
    path('',views.obtenerlista, name='index'),
    path('editar/', views.editar, name='editar'),
    # path('obtenerlista/', views.obtenerlista, name='obtenerlista'),
    path('guardar_producto/', views.guardar_producto, name='guardar_producto')
]