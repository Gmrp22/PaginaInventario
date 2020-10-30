from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', main, name="main"),
    path('agregar/', agregarProducto, name="agregarProducto"),
    path('eliminar/', eliminarProducto.as_view(), name="eliminarProducto"),
    path('listar/', listaGeneral.as_view(), name="listageneral"),
    path('confirmar/(?P<pk>\d+)/', eliminar.as_view(), name="confirmarProducto"),

    path('listarexistencia/', listaE.as_view(), name="listae"),
    path('listarfecha/', listaF.as_view(), name="listaf"),
    path('listarnombre/', listaN.as_view(), name="listan"),
]