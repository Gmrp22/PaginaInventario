from django.urls import path
from django.urls import path, include

from .views import *

urlpatterns = [
    path('index/', main, name="main"),
    path('agregar/', agregarProducto, name="agregarProducto"),
    

]