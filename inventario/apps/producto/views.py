from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from apps.producto.forms import ProductoForm
from apps.producto.models import Producto


def main(request):
    return render(request, 'producto/index.html')


def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("producto:main")
    else:
        form = ProductoForm()
    return render(request, 'producto/agregarProducto.html', {'form': form})

# return render(request, 'producto/agregarProducto.html')

class eliminar(DeleteView):
    model = Producto
    template_name = 'producto/confirmarEliminar.html'
    success_url = reverse_lazy("producto:eliminarProducto")

class eliminarProducto(ListView):
    model = Producto
    template_name = 'producto/eliminarProducto.html'

class listaGeneral(ListView):
    model = Producto
    template_name = 'producto/listaGeneral.html'


# class ProductoCreat(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'producto/index.html'
#     succes_url = reverse_lazy('producto:main')
