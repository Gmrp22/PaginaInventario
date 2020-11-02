from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', main, name="main"),
    path('agregar/', agregarProducto, name="agregarProducto"),
    path('eliminar/', eliminarProducto.as_view(), name="eliminarProducto"),
    path('listar/', listaGeneral.as_view(), name="listageneral"),
    path('confirmar/(?P<pk>\d+)/', eliminar.as_view(), name="confirmarProducto"),

    path('listarexistencia/', listaE, name="listae"),
    path('listarfecha/', listaF, name="listaf"),
    path('listarnombre/', listaN, name="listan"),
    path('listarpnombre/<nombre1>', listaPN, name="listapn"),
    path('listarpfecha/<nombre1>', listaPF, name="listapf"),
    path('listarpexistencia/<nombre1>', listaPE, name="listape"),
    path('dashboard/', pie_chart, name='pie-chart'),
]
