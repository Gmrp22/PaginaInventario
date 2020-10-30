from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        opciones = (('Perecedero', 'Perecedero'), ('No perecedero', 'No Perecedero'),)
        fields = ['nombre', 'existencia', 'dimension', 'descripcion',
                  'lote', 'Tipo', 'Fecha']
        labels = {
            'nombre': 'Nombre',
            'existencia': 'Existencia',
            'dimension': 'Dimension',
            'descripcion': 'Descripcion',
            'lote': 'Lote',
            'tipo': 'Tipo',
            'fecha': 'Fecha',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'existencia': forms.TextInput(attrs={'class': 'form-control'}),
            'dimension': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipo': forms.Select(attrs={'class': 'form-control', 'id': 'tipo'}, choices=opciones),
            'Fecha': forms.DateInput(format=('%m/%d/%Y'),
                                     attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date', 'id': 'fecha'}),

        }
