from django import forms
from .models import Reservas

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) > 80:
            raise forms.ValidationError("El nombre no puede superar los 80 caracteres.")
        return nombre

    def clean_cantidad_personas(self):
        cantidad_personas = self.cleaned_data.get('cantidad_personas')
        if cantidad_personas < 1 or cantidad_personas > 15:
            raise forms.ValidationError("La cantidad de personas debe estar entre 1 y 15.")
        return cantidad_personas
