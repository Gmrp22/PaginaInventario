from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from apps.producto.forms import ProductoForm, ProductoFormName, ProductoFormDate, ProductoFormExistencia
from apps.producto.models import Producto
from django.contrib import messages

def main(request):
    return render(request, 'producto/index.html')
def errora(request):
    return render(request, 'producto/errora.html')

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("producto:errora")
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


def listaPF(request, nombre1):
    productos = Producto.objects.filter(Fecha=nombre1)
    return render(request, 'producto/Fecha.html', {'productos': productos})


def listaF(request):
    if request.method == 'POST':
        form = ProductoFormDate(request.POST)
        # if form.is_valid():
        nombre1 = ''
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                nombre1 += value

        return redirect("producto:listapf", nombre1)
    else:
        form = ProductoFormDate()
    return render(request, 'producto/listaPorFecha.html', {'form': form})


def listaPE(request, nombre1):
    productos = Producto.objects.filter(existencia=nombre1)
    return render(request, 'producto/Existencia.html', {'productos': productos})


def listaE(request):
    if request.method == 'POST':
        form = ProductoFormExistencia(request.POST)
        # if form.is_valid():
        nombre1 = ''
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                nombre1 += value

        return redirect("producto:listape", nombre1)
    else:
        form = ProductoFormExistencia()
    return render(request, 'producto/listaPorExistencia.html', {'form': form})




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
                nombre1 += value

        return redirect("producto:listapn", nombre1)
    else:
        form = ProductoFormName()
    return render(request, 'producto/listaPorNombre.html', {'form': form})


# class ProductoCreat(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'producto/index.html'
#     succes_url = reverse_lazy('producto:main')
def pie_chart(request):
    labels = []
    data = []

    queryset = Producto.objects.order_by('existencia')[:5]
    for city in queryset:
        labels.append(city.nombre)
        data.append(city.existencia)

    return render(request, 'producto/dash.html', {
        'labels': labels,
        'data': data,
    })