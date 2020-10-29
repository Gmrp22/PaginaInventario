from django.shortcuts import render
#from django.shortcuts import HttpResponse

def main(request):
    return render(request,'producto/index.html')

def agregarProducto(request):
    return render(request,'producto/agregarProducto.html')

def eliminarProducto(request):
    return render(request,'producto/eliminarProducto.html')

def listaGeneral(request):
    return render(request,'producto/listaGeneral.html')