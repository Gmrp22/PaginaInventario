from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
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


def eliminarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return reverse_lazy('producto: main')
    else:
        form = ProductoForm()
    return render(request, 'producto/eliminarProducto.html', {'form': form})
    # def eliminarProducto(request):
 #   return render(request, 'producto/eliminarProducto.html')


def listaGeneral(request):
    return render(request, 'producto/listaGeneral.html')


# class ProductoCreat(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'producto/index.html'
#     succes_url = reverse_lazy('producto:main')
