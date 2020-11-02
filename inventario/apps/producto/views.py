from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from apps.producto.forms import ProductoForm, ProductoFormName, ProductoFormDate
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


class listaE(ListView):
    model = Producto
    template_name = 'producto/listaPorExistencia.html'


class listaF(ListView):
    model = Producto
    template_name = 'producto/listaPorFecha.html'


def listaPN(request, nombre1):
    productos = Producto.objects.filter(nombre=nombre1)
    return render(request, 'producto/Nombre.html', {'productos': productos})


def listaN(request):
    if request.method == 'POST':
        form = ProductoFormName(request.POST)
        # if form.is_valid():
        nombre1 = ''
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                nombre1 +=  value

        return redirect("producto:listapn",nombre1)
    else:
        form = ProductoFormName()
    return render(request, 'producto/listaPorNombre.html', {'form': form})

# class ProductoCreat(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'producto/index.html'
#     succes_url = reverse_lazy('producto:main')
